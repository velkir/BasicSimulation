from collections import deque
from PathFindAlgorithms.PathFinder import PathFinder

class BFS(PathFinder):
    def __init__(self, start_coordinate, target_coordinates=None, square_size=None, obstacles=None):
        # Конструктор класса. Инициализирует начальную точку, целевые точки, размер квадрата и препятствия.
        # Вызывает конструктор родительского класса (PathFinder).
        super().__init__(start_coordinate, target_coordinates, square_size, obstacles)

    def find_shortest_path(self):
        # Метод для нахождения кратчайшего пути до всех целевых точек.
        shortest_path = None
        shortest_distance = float('inf')

        for target in self.target_coordinates:
            self.target_coordinate = target
            path = self.findPath()
            if path and len(path) < shortest_distance:
                shortest_path = path
                shortest_distance = len(path)

        return shortest_path

    def find_all_paths(self):
        # Метод для нахождения всех путей до целевых точек.
        all_paths = []

        for target in self.target_coordinates:
            self.target_coordinate = target
            path = self.findPath()
            if path:
                all_paths.append(path)

        return all_paths

    def findPath(self):
        # Метод для поиска пути с помощью алгоритма BFS.
        # Реализация BFS не изменилась, она такая же, как в предыдущих ответах.
        queue = deque([(self.start_coordinate, [self.start_coordinate])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            x, y = current

            if current == self.target_coordinate:
                return path

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(x, y):
                neighbor_x, neighbor_y = neighbor
                if self.is_valid_cell(neighbor_x, neighbor_y, self.start_coordinate[0], self.start_coordinate[1], self.square_size):
                    queue.append((neighbor, path + [neighbor]))

        return None

    def is_valid_cell(self, x, y, center_x, center_y, size):
        # Проверяем, что клетка находится в квадрате с центром (center_x, center_y) и заданной длиной size
        # и не является препятствием
        return (
            abs(x - center_x) <= size and
            abs(y - center_y) <= size and
            (x, y) not in self.obstacles
        )

    def get_neighbors(self, x, y):
        # Возвращает список соседних клеток для клетки (x, y)
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# Тестирование
# start_point = (5, 5)
# target_points = [(7, 6), (4, 4), (2, 2)]
# center_point = (5, 5)
# square_size = 5
# obstacles = [(6, 5), (5, 6), (4, 5), (4, 4)]  # Список координат препятствий
#
# bfs = BFS(start_point, target_points, square_size, obstacles)
# shortest_path = bfs.find_shortest_path()
# all_paths = bfs.find_all_paths()
#
# if shortest_path:
#     print("Кратчайший маршрут до целевой точки:", shortest_path)
# else:
#     print("Кратчайший маршрут до целевой точки не найден.")
#
# print("Все маршруты до целевых точек:", all_paths)