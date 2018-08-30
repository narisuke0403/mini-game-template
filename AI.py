class AI:
    def __init__(self, field, situation):
        self.field = field
        self.situation = situation

    def decision(self):
        from random import uniform
        x, y = self.sample()
        if x ** 2 + y ** 2 > 1:
            return "value Error"
        else:
            return x + uniform(-0.1, 0.1), y + uniform(-0.1, 0.1)

    def thinking(self):
        action = [0, 0]
        return action[0], action[1]

    def sample(self):
        from Player import Player
        from math import cos, sin, radians, sqrt
        from random import random, randint, uniform
        score = -100
        action = [0, 0]

        for i in range(100):
            template_player = Player(self.situation[0], self.situation[1])
            for t in range(2):
                d = random()
                r = radians(randint(0, 359))
                noise_x, noise_y = uniform(-0.5, 0.5), uniform(-0.5, 0.5)
                if t == 0:
                    template_action = [d * cos(r), d * sin(r)]
                template_player.simulation_move(d * cos(r) + noise_x, d * sin(r) + noise_y)
                if self.field.check_state(template_player) == "gameover" \
                        or self.field.check_state(template_player) == "clear":
                    break

            state = self.field.check_state(template_player)
            if state == "gameover":
                template_score = -100
            elif state == "playing":
                goal_position_x = self.field.goal_position_x + 0.5
                goal_position_y = self.field.goal_position_y + 0.5
                template_score = -sqrt((goal_position_x - template_player.position_x) ** 2 + (goal_position_y - template_player.position_y) ** 2)
            else:
                template_score = 1

            if score < template_score:
                score = template_score
                action = template_action

        return action[0], action[1]
