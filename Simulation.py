import Actions.initActions.Entities_positioner
from Actions.turnActions.Entities_mover import Entities_mover
import Renderers
class Simulation:
    def __init__(self, renderer, actions):
        self.map = None
        self.renderer = renderer
        self.actions = actions
        self.turn = 0

    def startSimulation(self):
        for initAction in self.actions[0]:
            initAction.make_init_action(simulation=self)
        self.renderer.render(self.map)
        while self.turn != 5:
            self.nextTurn()
            self.renderer.render(self.map)

    def nextTurn(self):
        for turnAction in self.actions[1]:
            turnAction.make_turn_action(simulation=self)

    def pauseSimulation(self):
        pass

