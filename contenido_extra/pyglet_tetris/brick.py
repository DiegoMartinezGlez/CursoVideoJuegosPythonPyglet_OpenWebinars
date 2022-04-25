import pyglet
from config import BRICK_WIDTH

class Brick:
    def __init__(self, x, y, color):
        self.x          = x
        self.y          = y
        self.color      = color
        self.rect       = pyglet.shapes.Rectangle(x, y, BRICK_WIDTH, BRICK_WIDTH, color=self.color)

    def move_right(self):
        self.x = self.x + 1

    def move_left(self):
        self.x = self.x - 1

    def move_down(self):
        self.y = self.y - 1