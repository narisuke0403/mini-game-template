class Field:

    def __init__(self, length=10, hole_position_x=2, hole_position_y=2, goal_position_x=9, goal_position_y=9):
        self.length = length
        self.hole_position_x = hole_position_x
        self.hole_position_y = hole_position_y
        self.goal_position_x = goal_position_x
        self.goal_position_y = goal_position_y

    def make_random_map(self):
        from random import randint
        self.length = randint(10, 20)
        self.hole_position_x = randint(2, self.length - 3)
        self.hole_position_y = randint(2, self.length - 3)
        self.goal_position_x = self.length - 1
        self.goal_position_y = self.length - 1

    def check_state(self, player):
        hole_length = 3
        goal_length = 1
        if player.position_x < 0 or player.position_x > self.length or player.position_y < 0 or player.position_y > self.length:
            return "gameover"
        elif player.position_x > self.hole_position_x and player.position_x < self.hole_position_x + hole_length and player.position_y > self.hole_position_y and player.position_y < self.hole_position_y + hole_length:
            return "gameover"
        elif player.position_x > self.goal_position_x and player.position_x < self.goal_position_x + goal_length and player.position_y > self.goal_position_y and player.position_y < self.goal_position_y + goal_length:
            return "clear"
        else:
            return "playing"
