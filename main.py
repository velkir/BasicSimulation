from Simulation import Simulation
from Map import Map
from Renderers.BasicConsoleRenderer import BasicConsoleRenderer
from Actions.turnActions.Entities_mover import Entities_mover
from Actions.turnActions.TurnCounter import TurnCounter
from Actions.initActions.Entities_positioner import Entities_positioner

renderer = BasicConsoleRenderer()

positioner = Entities_positioner()
mover = Entities_mover()
turncounter = TurnCounter()

initActions = [positioner]
turnActions = [mover, turncounter]

actions = [initActions, turnActions]

simulation = Simulation(renderer=renderer, actions=actions)
simulation.startSimulation()

