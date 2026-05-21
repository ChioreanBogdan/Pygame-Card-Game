class TurnManager:
    def __init__(self):
        self.current_turn = 1
        self.player_turn = True

    def end_turn(self):
        self.current_turn += 1
        self.player_turn = not self.player_turn