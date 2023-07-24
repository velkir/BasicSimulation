import Coordinates
import Map
import Settings
from Entities.Nature.Grass import Grass
from Entities.Nature.Tree import Tree
from Entities.Nature.Rock import Rock
from Entities.Creatures.Herbivore.Pig import Pig
from Entities.Creatures.Predators.Wolf import Wolf
import random

class Entities_positioner:
    def __init__(self):
        settings = Settings.Settings()
        self.grass = settings.grass
        self.rocks = settings.rocks
        self.trees = settings.trees
        self.pigs = settings.pigs
        self.pig_speed = settings.pig_speed
        self.pig_hp = settings.pig_hp
        self.wolves = settings.wolves
        self.wolf_speed = settings.wolf_speed
        self.wolf_hp = settings.wolf_hp
        self.map_width = settings.width
        self.map_height = settings.height

    def position_entities(self, simulation):
        map = Map.Map(self.map_width, self.map_height)
        for _ in range(int(self.grass)):
            grass = Grass(self.random_coordinates(map))
            map.map[grass.coordinates.coordinates]=grass
        for _ in range(int(self.trees)):
            tree = Tree(self.random_coordinates(map))
            map.map[tree.coordinates.coordinates]=tree
        for _ in range(int(self.rocks)):
            rock = Rock(self.random_coordinates(map))
            map.map[rock.coordinates.coordinates]=rock
        for _ in range(int(self.pigs)):
            pig = Pig(self.random_coordinates(map), speed=self.pig_speed, hp=self.pig_hp)
            map.map[pig.coordinates.coordinates]=pig
        for _ in range(int(self.wolves)):
            wolf = Wolf(self.random_coordinates(map), speed=self.wolf_speed, hp=self.wolf_hp)
            map.map[wolf.coordinates.coordinates]=wolf
        simulation.map = map

    def random_coordinates(self, map):
        def is_empty(x, y):
            if (x, y) not in map.map:
                return (random_x, random_y)
        tries = 0
        while tries != 50:
            random_x = random.randint(0, int(self.map_width)-1)
            random_y = random.randint(0, int(self.map_height)-1)
            if is_empty(random_x, random_y):
                return Coordinates.Coordinates(random_x, random_y)

    def make_init_action(self, simulation):
        self.position_entities(simulation)



