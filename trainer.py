# -*- coding: utf-8 -*-
from gym import make
from numpy import zeros, argmax
import agent
import time

class Trainer:
    def __init__(self, epsilon, algorithm, min_epsilon, episodes, max_steps, alpha, gamma):
        # Creating hyperparameters
        self.MAX_NUM_EPISODES = episodes
        self.STEPS_PER_EPISODE = max_steps
        self.EPSILON_MIN = min_epsilon
        self.MAX_NUM_STEPS = self.MAX_NUM_EPISODES * self.STEPS_PER_EPISODE
        self.EPSILON = epsilon
        if min_epsilon != None:
            # self.EPSILON_DECAY = 500 * self.EPSILON_MIN / self.MAX_NUM_STEPS
            self.EPSILON_DECAY = 3*(self.EPSILON/ self.MAX_NUM_STEPS)
        else:
            self.EPSILON_DECAY = None
        self.ALPHA = alpha
        self.GAMMA = gamma
        self.OBS_BINS= 30
        
        # Creating the environment
        self.env = make("MountainCar-v0")
        
        # Getting the observation and action space shapes and other info
        self.obs_shape = self.env.observation_space.shape
        self.obs_high = self.env.observation_space.high
        self.obs_low = self.env.observation_space.low
        self.action_shape = self.env.action_space.n
        
        # We get the width of each bin
        self.bin_width = (self.obs_high-self.obs_low)/self.OBS_BINS
        
        # Creating the Q-Matrix:
        # The observation space for this problem is a Box(2,) (vectors on R2),
        # and each parameter is continuos. The actions space is Discrete(3). 
        # To simplify the problem and get better
        # and faster convergence, we will discretize each observation parameter in 30 bins.
        # Thats why the Q-Matrix is 31x31x3
        self.Q = zeros((self.OBS_BINS+1, self.OBS_BINS+1, self.action_shape)) 
        
        # Creating the agent
        self.agent = agent.Agent(algorithm,epsilon,min_epsilon,self.EPSILON_DECAY,self.Q,self.action_shape,alpha,gamma)


    # Method to discretize the observations: R2 continuous --> R2 discrete
    def discretize(self, obs):
        return tuple(((obs-self.obs_low)/self.bin_width).astype(int))
        
    def test(self):
        environment = make("MountainCar-v0")
        done = False
        obs = environment.reset()
        total_reward = 0.0
        while not done:
            environment.render()
            time.sleep(0.001)
            action = self.best_policy[self.discretize(obs)] #acción que dictamina la política que hemos entrenado
            next_obs, reward, done, info = environment.step(action)
            obs = next_obs
            total_reward += reward
        environment.close()
        return total_reward
    
    def StartTraining(self):
        self.outputList = []
        best_reward = -float('inf')
        for episode in range(self.MAX_NUM_EPISODES):
            done = False
            obs = self.env.reset()
            total_reward = 0.0
            while not done:
                action = self.agent.get_action(self.discretize(obs))# Acción elegida según la ecuación de Q-LEarning
                next_obs, reward, done, info = self.env.step(action)
                self.agent.learn(self.discretize(obs), action, reward, self.discretize(next_obs))
                obs = next_obs
                total_reward += reward
            if total_reward > best_reward:
                best_reward = total_reward
            print("Episode #{}. Total Reward: {}. Best Reward: {}. Epsilon Value: {}".format(episode, total_reward, best_reward, self.agent.epsilon))
            self.outputList.append(str(episode)+","+str(total_reward)+","+str(best_reward)+","+str(self.agent.epsilon)+"\n")
        
        ## De todas las políticas de entrenamiento que hemos obtenido devolvemos la mejor de todas
        self.env.close()
        self.best_policy = argmax(self.agent.Q, axis = 2)
        return self.best_policy
    
    
    def GenerateOutput(self):
        output = open("output.txt", "w")
        for line in self.outputList:
            output.write(line)
        output.close()