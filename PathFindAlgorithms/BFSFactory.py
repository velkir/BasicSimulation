from PathFindAlgorithms.BFS import BFS
from PathFindAlgorithms.PathFinderFactory import PathFinderFactory


class BFSFactory(PathFinderFactory):
    def createPathFinder(self, start_coordinate, target_coordinates, square_size, obstacles):
        return BFS(start_coordinate, target_coordinates, square_size, obstacles)