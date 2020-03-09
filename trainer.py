# -*- coding: utf-8 -*-
from gym import make

class Trainer:
    def __init__(self, epsilon, algorithm, min_epsilon, episodes, max_steps, alpha, gamma):
        self.MAX_NUM_EPISODES = episodes
        self.STEPS_PER_EPISODE = max_steps
        self.EPSILON_MIN = min_epsilon
        self.MAX_NUM_STEPS = self.MAX_NUM_EPISODES * self.STEPS_PER_EPISODE
        self.EPSILON = epsilon
        self.EPSILON_DECAY = 500 * self.EPSILON_MIN / self.MAX_NUM_STEPS
        self.ALPHA = alpha
        self.GAMMA = gamma
        self.NUM_DISCRETE_BINS = 30
        
        
    def StartTraining():
        return "Bestpolicy"