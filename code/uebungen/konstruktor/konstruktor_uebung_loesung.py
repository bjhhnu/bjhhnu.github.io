import random


class Zombie:

    attribute_list = ["Grausame:r", "Verdorbene:r", "Ausgestossene:r"]
    job_list = ["Jäger:in", "Lehrer:in", "Bauarbeiter:in"]

    def __init__(self):
        self.name = self.generate_zombie_name()

    def generate_zombie_name(self):
        random_attribute = random.choice(self.attribute_list)
        random_job = random.choice(self.job_list)
        return "%s %s" % (random_attribute, random_job)
