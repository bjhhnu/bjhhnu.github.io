from zombie import Zombie
import numpy as np
# pip install numpy


class ChaosZombie(Zombie):
    def __init__(self, variance, mean):
        # TODO Rufe den Superkonstruktor auf
        self.variance = variance
        self.mean = mean

    def eat_brain(self):
        return np.random.normal(loc=TODO, scale=TODO)
