import random


class Zombie:

    ZOMBIE_QUESTION = "Der Zombie %s stellt dir die folgende Frage: %s"
    ZOMBIE_SUCCESS_QUESTION = "Der Zombie ist beeindruckt von deinem Wissen, isst %s Prozent deines Gehirns und geht " \
                              "weiter.\n "
    ZOMBIE_FAIL_QUESTION = "Der Zombie humpelt stöhnend weiter. Er interessiert sich nicht für den Gehirn.\n"
    attribute_list = ["Grausame:r", "Verdorbene:r", "Ausgestossene:r"]
    job_list = ["Jäger:in", "Lehrer:in", "Bauarbeiter:in"]

    def __init__(self):
        self.name = self.generate_zombie_name()

    def generate_zombie_name(self):
        return "%s %s" % (random.choice(self.attribute_list), random.choice(self.job_list))

    def eat_brain(self):
        return 1


