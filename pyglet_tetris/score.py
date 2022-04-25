import pyglet
from config import *
from block import Block

class Score:
    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.width      = PANELS_WIDTH
        self.border     = 10
        panel_height    = 6*BRICK_WIDTH
        rect_x = x-BRICK_WIDTH//2
        rect_y = y-panel_height//2 - BRICK_WIDTH//2
        self.rect_out   = pyglet.shapes.Rectangle(rect_x, rect_y, PANELS_WIDTH, panel_height, color=BLACK_COLOR)
        self.rect_in    = pyglet.shapes.Rectangle(rect_x+self.border, rect_y+self.border, PANELS_WIDTH-self.border*2, panel_height-self.border*2, color=BG_COLOR)
        self.label      = pyglet.text.Label('BLOCKS COUNTER 0', font_name='Joystix Monospace', font_size=24, 
                            x=self.x+BRICK_WIDTH, y=self.y+BRICK_WIDTH,
                            color=BLACK_COLOR2,
                            anchor_x='left', anchor_y='center')
        self.label2     = pyglet.text.Label('LINES CLEARED 0', font_name='Joystix Monospace', font_size=24, 
                            x=self.x+BRICK_WIDTH, y=self.y-BRICK_WIDTH,
                            color=BLACK_COLOR2,
                            anchor_x='left', anchor_y='center')

    def draw(self):
        self.rect_out.draw()
        self.rect_in.draw()
        self.label.draw()
        self.label2.draw()

    def update_blocks(self, num):
        self.label.text = "BLOCKS COUNTER "+str(num)

    def update_lines(self, num):
        self.label2.text = "LINES CLEARED "+str(num)