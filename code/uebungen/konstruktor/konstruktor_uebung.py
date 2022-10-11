import random


class Zombie:

    attribute_list = ["Grausame:r", "Verdorbene:r", "Ausgestossene:r"]
    # TODO: Ergänze eine weitere liste für mögliche Jobs (1 Zeile)

    def __init__(self):
        self.name = # TODO richtiger Aufruf (1 Zeile)

    def generate_zombie_name(self):
        # TODO Wähle ein zufälliges Element aus jeder Liste. Verwende z.B. random.choice (die random
        # Bibliothek ist bereits importiert (2 Zeilen)
        return "%s %s" % (random_attribute, random_job)
