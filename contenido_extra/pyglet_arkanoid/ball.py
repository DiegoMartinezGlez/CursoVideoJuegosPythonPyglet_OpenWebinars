import pyglet
import random
from config import *

class Ball():
    def __init__(self, x, y, width):
        self.width      = width

        self.topSpeed   = 8.0
        self.minSpeed   = 2.0
        self.vel_x      = 0.0
        self.vel_y      = 0.0

        self.circle     = pyglet.shapes.Circle(x, y, self.width, color=COLOR_BLUE)

        # init!
        self.push()

    def draw(self):
        self.circle.draw()

    def update(self, dt):
        self.circle.x   += self.vel_x
        self.circle.y   += self.vel_y

    def push(self):
        self.vel_y = random.randint(-self.topSpeed, self.topSpeed)
        self.vel_x = random.randint(-self.topSpeed, self.topSpeed)

    def reboundX(self):
        self.vel_x = -self.vel_x

    def reboundY(self, vel):
        
        self.vel_y = -self.vel_y

