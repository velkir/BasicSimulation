from Entities.Creatures.Herbivore import Herbivore
from Behavior.Decision import Decision
import Coordinates

class Pig(Herbivore.Herbivore):
    def __init__(self, coordinates, speed, hp):
        super().__init__(coordinates, speed, hp)
        self.ascii_image = "🐷"
        self.line_of_sight_distance = 3
    def analyze(self) -> Decision:
        # print(type(self.coordinates.coordinates))
        (x, y) = self.coordinates.coordinates
        x += 1
        return Decision(Coordinates.Coordinates(x, y), "move")


