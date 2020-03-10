# -*- coding: utf-8 -*-
import numpy as np

class Agent:
    def __init__(self, algorithm,epsilon,epsilon_min,epsilon_decay,Q,action_shape,alpha,gamma):
        self.algorithm = algorithm
        self.epsilon = epsilon
        self.EPSILON_MIN = epsilon_min
        self.EPSILON_DECAY = epsilon_decay
        self.Q = Q
        self.action_shape = action_shape
        self.alpha = alpha
        self.gamma = gamma
    
    def get_action(self, discrete_obs):
        if self.algorithm == "Greedy":
            return np.argmax(self.Q[discrete_obs])
        elif self.algorithm == "EpsilonGreedy":
            if np.random.random() > self.epsilon: #Con probabilidad 1-epsilon, elegimos la mejor posible
                return np.argmax(self.Q[discrete_obs])
            else:
                return np.random.choice([a for a in range(self.action_shape)])#Con probabilidad epsilon, elegimos una al azar
        else:
            # Selección de la acción en base a Epsilon-Greedy
            if self.epsilon > self.EPSILON_MIN:
                self.epsilon -= self.EPSILON_DECAY
            if np.random.random() > self.epsilon: #Con probabilidad 1-epsilon, elegimos la mejor posible
                return np.argmax(self.Q[discrete_obs])
            else:
                return np.random.choice([a for a in range(self.action_shape)])#Con probabilidad epsilon, elegimos una al azar
        
        
    def learn(self, discrete_obs, action, reward, discrete_next_obs):
        self.Q[discrete_obs][action] += self.alpha*(reward + self.gamma * np.max(self.Q[discrete_next_obs]) - self.Q[discrete_obs][action])
        
        
        
        
        
        