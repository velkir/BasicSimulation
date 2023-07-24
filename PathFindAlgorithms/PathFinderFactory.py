from abc import ABC, abstractmethod


class PathFinderFactory(ABC):
    @abstractmethod
    def createPathFinder(self, start_coordinate, target_coordinates, square_size, obstacles):
        pass