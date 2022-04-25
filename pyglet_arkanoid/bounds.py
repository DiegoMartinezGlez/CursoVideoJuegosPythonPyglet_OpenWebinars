import pyglet
from config import *

# this class draws the game zone, a white rectangle with black border
# contains methods to check collisions

class Bounds():
    def __init__(self, width):
        self.width      = width        
        self.outer_rect = pyglet.shapes.Rectangle(WINDOW_WIDTH//2 - self.width//2, 0, self.width, WINDOW_HEIGHT, color=COLOR_BLACK)
        inner_width     = self.width - BOUNDS_WIDTH*2
        self.inner_rect = pyglet.shapes.Rectangle(WINDOW_WIDTH//2 - (inner_width//2), 0, inner_width, WINDOW_HEIGHT-BOUNDS_WIDTH, color=COLOR_WHITE)

    def draw(self):        
        self.outer_rect.draw()
        self.inner_rect.draw()

    def checkLeftSideIn(self, x):
        return x>self.inner_rect.x

    def checkRightSideIn(self, x):
        return x<self.inner_rect.x+self.inner_rect.width

    def checkTopSideIn(self, y):
        return y<self.inner_rect.y+self.inner_rect.height

    def getLeftX(self):
        return self.inner_rect.x

    def getRightX(self):
        return self.inner_rect.x+self.inner_rect.width

