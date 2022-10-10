import random


class Zombie:
    attribute_list = ["a", "b"]
    job_list = ["Jäger", "Lehrer"]

    def __init__(self):
        self.name = self.create_name()

    def create_name(self):
        return "%s %s" % (random.choice(self.attribute_list), random.choice(self.job_list))

    def eat_brain(self):
        return 1


