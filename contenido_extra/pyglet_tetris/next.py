import pyglet
from config import *
from block import Block

class Next:
    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.width      = PANELS_WIDTH
        self.border     = 10
        panel_height    = 4*BRICK_WIDTH
        rect_x = x-BRICK_WIDTH//2
        rect_y = y-panel_height//2 - BRICK_WIDTH//2
        self.rect_out   = pyglet.shapes.Rectangle(rect_x, rect_y, PANELS_WIDTH, panel_height, color=BLACK_COLOR)
        self.rect_in    = pyglet.shapes.Rectangle(rect_x+self.border, rect_y+self.border, PANELS_WIDTH-self.border*2, panel_height-self.border*2, color=BG_COLOR)
        self.label      = pyglet.text.Label('NEXT BLOCK', font_name='Joystix Monospace', font_size=24, 
                            x=self.x+ BRICK_WIDTH*2, y=self.y-BRICK_WIDTH//2,
                            color=BLACK_COLOR2,
                            anchor_x='left', anchor_y='center')
        self.block      = None
        
    def draw(self):
        self.rect_out.draw()
        self.rect_in.draw()
        self.label.draw()
        if self.block is not None and self.label.content_width is not None:
            for brick in self.block.bricks:
                brick.rect.x = self.x + BRICK_WIDTH*3 + self.label.content_width + brick.x*BRICK_WIDTH
                brick.rect.y = self.y + BRICK_WIDTH//2 - brick.y*BRICK_WIDTH
                brick.rect.draw()

    def set_next(self, type):
        self.block = Block(3, 2, type)

