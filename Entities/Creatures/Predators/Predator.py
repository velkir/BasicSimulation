from Entities import Creature
from Behavior.Decision import Decision

class Predator(Creature.Creature):
    def __init__(self, coordinates, speed, hp):
        super().__init__(coordinates, speed, hp)

    def makeAction(self):
        decision = self.analyze()
        if decision.action == "move":
            self.move(decision.coordinates)
        elif decision.action == "attack":
            self.attack(decision.coordinates)
        elif decision.action == "sleep":
            self.sleep()

    def analyze(self) -> Decision:
        return Decision(coordinates=self.coordinates, action=None)

    def attack(self, coordinates):
        pass

