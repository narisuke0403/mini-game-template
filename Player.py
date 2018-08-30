from AI import AI


class Player:
    def __init__(self, *args,):
        if len(args) != 0:
            self.position_x = args[0]
            self.position_y = args[1]
        else:
            self.position_x = 0.0
            self.position_y = 0.0

    def move(self, field, situation):
        player_ai = AI(field, situation)
        move_x, move_y = player_ai.decision()
        self.position_x += move_x
        self.position_y += move_y

    def simulation_move(self, x, y):
        self.position_x += x
        self.position_y += y
