class TurnCounter:
    def make_turn_action(self, simulation):
        simulation.turn += 1
        print(f"Turn:{simulation.turn}")