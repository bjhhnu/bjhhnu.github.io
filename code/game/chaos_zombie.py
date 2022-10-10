from zombie import Zombie
import numpy as np


class ChaosZombie(Zombie):
    def __init__(self, variance, mean):
        super(ChaosZombie, self).__init__()
        self.variance = variance
        self.mean = mean

    def eat_brain(self):
        return np.random.normal(loc=self.mean, scale=self.variance)
