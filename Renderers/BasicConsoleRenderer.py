class BasicConsoleRenderer:
    def render(self, _map):
        for y in range(_map.height):
            for x in range(_map.width):
                if (x, y) in _map.map:
                    # print(_map.map[(x, y)].coordinates.coordinates)
                    print(_map.map[(x, y)].ascii_image, end='')
                else:
                    print('.', end='')
            print()