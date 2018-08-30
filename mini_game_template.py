from Field import Field
from Player import Player
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics import Ellipse
from kivy.properties import NumericProperty
from kivy.clock import Clock

Config.set("graphics", "width", "450")
Config.set("graphics", "height", "450")


class Draw(Widget):

    count = NumericProperty(0)

    def __init__(self, player, field, **kwargs):
        super(Draw, self).__init__(**kwargs)
        self.player = player
        self.field = field
        self.n = 0

    def move(self, n):
        with self.canvas:
            if self.n < len(self.player):
                self.canvas.clear()
                Line(points=[50, 50,
                             50 + self.field.length * 20, 50,
                             50 + self.field.length * 20, 50 + self.field.length * 20,
                             50, 50 + self.field.length * 20],
                     close="True")
                Line(points=[50 + self.field.hole_position_x * 20, 50 + self.field.hole_position_y * 20,
                             50 + self.field.hole_position_x * 20 + 3 * 20, 50 + self.field.hole_position_y * 20,
                             50 + self.field.hole_position_x * 20 + 3 * 20, 50 + self.field.hole_position_y * 20 + 3 * 20,
                             50 + self.field.hole_position_x * 20, 50 + self.field.hole_position_y * 20 + 3 * 20],
                     close="True")
                Line(points=[50 + self.field.length * 20 - 20, 50 + self.field.length * 20 - 20,
                             50 + self.field.length * 20,  50 + self.field.length * 20 - 20,
                             50 + self.field.length * 20, 50 + self.field.length * 20,
                             50 + self.field.length * 20 - 20, 50 + self.field.length * 20],
                     close="True")
                Ellipse(pos=(self.player[n][0]*20+50, self.player[n][1]*20+50), size=(10, 10))

    def update(self, dt):
        if self.n < len(self.player):
            self.n = self.n + 1
            self.move(self.n)


class DrawApp(App):

    def __init__(self, player, field, **kwargs):
        super(DrawApp, self).__init__(**kwargs)
        self.player = player
        self.field = field

    def build(self):
        d = Draw(self.player, self.field)
        Clock.schedule_interval(d.update, 1.0/2)
        return d


def main():
    field = Field()
    player = Player()
    turn = 0
    history = []
    # field.make_random_map()
    while field.check_state(player) == "playing":
        situation = [player.position_x, player.position_y]
        player.move(field, situation)
        history.append([player.position_x, player.position_y])
        print(player.position_x)
        print(player.position_y)
        turn += 1
    print(field.check_state(player))
    print("turn = {}".format(turn))
    a = DrawApp(history, field)
    a.run()


if __name__ == '__main__':
    main()
