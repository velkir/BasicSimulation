from collections import deque
from abc import ABC, abstractmethod


class PathFinder(ABC):
    def __init__(self, start_coordinate, target_coordinates, square_size, obstacles=None):
        self.start_coordinate = start_coordinate
        self.target_coordinates = target_coordinates
        self.square_size = square_size
        self.obstacles = set(obstacles) if obstacles else set()

    @abstractmethod
    def findPath(self):
        pass

    @abstractmethod
    def find_all_paths(self):
        pass

    @abstractmethod
    def find_shortest_path(self):
        pass
