from zombie import Zombie
from question import Question
import numpy as np


class ChaosZombie(Zombie):

    def __init__(self, variance, mean, question):
        super(ChaosZombie, self).__init__()
        self.variance = variance
        self.mean = mean
        self.question = question

    def eat_brain(self):
        return round(np.random.normal(loc=self.mean, scale=self.variance), 2)
