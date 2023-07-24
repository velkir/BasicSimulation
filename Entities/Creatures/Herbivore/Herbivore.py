from Entities import Creature


class Herbivore(Creature.Creature):
    def __init__(self, coordinates, speed, hp):
        super().__init__(coordinates, speed, hp)

    def eat(self):
        pass

    def makeAction(self):
        decision = self.analyze()
        if decision.action == "move":
            self.move(decision.coordinates)
        elif decision.action == "sleep":
            self.sleep()
        elif decision.action == "eat":
            self.eat()


