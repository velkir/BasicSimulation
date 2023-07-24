from Entities.Creature import Creature
from Entities.Creatures.Predators.Wolf import Wolf
from Entities.Creatures.Herbivore.Pig import Pig

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = {}

    def getCreatures(self):
        creatures = []
        for coordinates, entity in self.map.items():
            if isinstance(entity, Creature):
                objects = entity.get_line_of_sight(self.map)
                if coordinates in objects:
                    objects.pop(coordinates)
                entity.line_of_sight = objects
                creatures.append(entity)
        return creatures


