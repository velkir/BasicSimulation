from Entities.Creatures.Predators import Predator
from Behavior.Decision import Decision

class Wolf(Predator.Predator):
    def __init__(self, coordinates, speed, hp):
        super().__init__(coordinates=coordinates, speed=speed, hp=hp)
        self.ascii_image = "🐺"
        self.line_of_sight_distance = 3
    def analyze(self) -> Decision:
        return Decision(self.coordinates, "sleep")







