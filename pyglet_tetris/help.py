import pyglet
from config import *

class Help:
    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.width      = PANELS_WIDTH
        self.border     = 10
        panel_height    = 6*BRICK_WIDTH
        rect_x = x-BRICK_WIDTH//2
        rect_y = y-panel_height//2 - 3*BRICK_WIDTH//2
        self.rect_out   = pyglet.shapes.Rectangle(rect_x, rect_y, PANELS_WIDTH, panel_height, color=BLACK_COLOR)
        self.rect_in    = pyglet.shapes.Rectangle(rect_x+self.border, rect_y+self.border, PANELS_WIDTH-self.border*2, panel_height-self.border*2, color=BG_COLOR)
        self.label      = pyglet.text.Label('HOW TO PLAY', font_name='Joystix Monospace', font_size=24, 
                            x=self.x+PANELS_WIDTH//2, y=self.y-BRICK_WIDTH//2,
                            color=BLACK_COLOR2,
                            anchor_x='center', anchor_y='center')
        self.label2     = pyglet.text.Label('MOVE BLOCKS WITH ARROW KEYS', font_name='Joystix Monospace', font_size=20, 
                    x=self.x+PANELS_WIDTH//2, y=self.y-4*BRICK_WIDTH//2,
                    color=BLACK_COLOR2,
                    anchor_x='center', anchor_y='center')
        self.label3     = pyglet.text.Label('PRESS SPACE TO ROTATE', font_name='Joystix Monospace', font_size=20, 
                    x=self.x+PANELS_WIDTH//2, y=self.y-6*BRICK_WIDTH//2,
                    color=BLACK_COLOR2,
                    anchor_x='center', anchor_y='center')
        
    def draw(self):
        self.rect_out.draw()
        self.rect_in.draw()
        self.label.draw()
        self.label2.draw()
        self.label3.draw()
