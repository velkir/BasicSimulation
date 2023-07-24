from Entities import Entity
from Behavior.Decision import Decision


class Creature(Entity.Entity):
    def __init__(self, coordinates, speed, hp):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp
        self.line_of_sight = None
        self.line_of_sight_distance = None
    def makeAction(self):
        pass

    def analyze(self) -> Decision:
        pass

    def move(self, coordinates):
        self.coordinates = coordinates

    def sleep(self):
        pass

    def get_line_of_sight(self, _map):
        def get_entities():
            entities = {}
            for i in range(self.line_of_sight_distance):
                for a in range(self.line_of_sight_distance):
                    if (self.coordinates.coordinates[0] + i - 1, self.coordinates.coordinates[1] + a - 1) in _map:
                        entities[self.coordinates.coordinates[0] + i - 1, self.coordinates.coordinates[1] + a - 1] = \
                        _map[self.coordinates.coordinates[0] + i - 1, self.coordinates.coordinates[1] + a - 1]
                    elif (self.coordinates.coordinates[0] - i - 1, self.coordinates.coordinates[1] - a - 1) in _map:
                        entities[self.coordinates.coordinates[0] - i - 1, self.coordinates.coordinates[1] - a - 1] = \
                        _map[self.coordinates.coordinates[0] - i - 1, self.coordinates.coordinates[1] - a - 1]
            return entities
        return get_entities()