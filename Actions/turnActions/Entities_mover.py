import Coordinates
import Map
from Entities.Nature.Grass import Grass
from Entities.Nature.Tree import Tree
from Entities.Nature.Rock import Rock
from Entities.Creatures.Herbivore.Pig import Pig
from Entities.Creatures.Predators.Wolf import Wolf

class Entities_mover():
    def moveAllCreatures(self, simulation):
        for creature in simulation.map.getCreatures():
            oldcoordinates=creature.coordinates.coordinates
            creature.makeAction()
            del simulation.map.map[oldcoordinates]
            simulation.map.map[creature.coordinates.coordinates]=creature

    def update(self, _map):
        self.creatures = _map.getCreatures()
        self.update_line_of_sight(_map)
    def update_line_of_sight(self, _map):
        for creature in self.creatures:
            creature.line_of_sight = creature.get_line_of_sight(_map.map)

    def make_turn_action(self, simulation):
        self.update(simulation.map)
        self.moveAllCreatures(simulation)

