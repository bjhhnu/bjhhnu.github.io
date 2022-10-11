class Zombie:
    # Klassenvariable
    kind = 'standard-level'

    def __init__(self, name):
        # Instanzvariable
        self.name = name


frankenstein = Zombie('Frankenstein')
print(frankenstein.name)
# >>> Frankenstein

walking_dead = Zombie('Walking Dead')
print(frankenstein.kind)
print(walking_dead.kind)
