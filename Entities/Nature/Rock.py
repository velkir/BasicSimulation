import Entities.Entity


class Rock(Entities.Entity.Entity):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.ascii_image = "🪨"