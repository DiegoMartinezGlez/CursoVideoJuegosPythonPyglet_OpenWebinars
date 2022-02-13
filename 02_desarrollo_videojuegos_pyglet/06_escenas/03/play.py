import pyglet
from pyglet.window import key
import config
from scene import Scene
from button import Button

class Play(Scene):
    def __init__(self, manager, id):
        self.manager    = manager
        self.id         = id
        self.batch      = pyglet.graphics.Batch()
        self.rect01     = pyglet.shapes.Rectangle(manager.window.width//2 - 50, manager.window.height//8 - 10, 20, 20, color=(0, 0, 0), batch=self.batch)
        self.rect_x_move = 'IDLE'
        self.rect_y_move = 'IDLE'
        self.rect_left   = False
        self.rect_right  = False
        self.rect_up     = False
        self.rect_down   = False
        self.rect_speed  = 5

    def on_draw(self):
        super().on_draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.rect_left = True
        if symbol == key.D:
            self.rect_right  = True
        if symbol == key.W:
            self.rect_up = True
        if symbol == key.S:
            self.rect_down  = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.rect_left = False
        if symbol == key.D:
            self.rect_right  = False
        if symbol == key.W:
            self.rect_up = False
        if symbol == key.S:
            self.rect_down  = False


    def update(self, dt):
        if (self.rect_left and self.rect_right) or (not self.rect_left and not self.rect_right):
            self.rect_x_move = 'IDLE'
        else:
            if self.rect_left:
                self.rect_x_move = 'LEFT'
            if self.rect_right:
                self.rect_x_move = 'RIGHT'

        if self.rect_x_move == 'LEFT':
            self.rect01.x -= self.rect_speed
        if self.rect_x_move == 'RIGHT':
            self.rect01.x += self.rect_speed

        if (self.rect_up and self.rect_down) or (not self.rect_up and not self.rect_down):
            self.rect_y_move = 'IDLE'
        else:
            if self.rect_up:
                self.rect_y_move = 'UP'
            if self.rect_down:
                self.rect_y_move = 'DOWN'
        
        if self.rect_y_move == 'DOWN':
            self.rect01.y -= self.rect_speed
        if self.rect_y_move == 'UP':
            self.rect01.y += self.rect_speed

    def loadScene(self):
        pyglet.gl.glClearColor(*(255, 255, 255, 255))

    def exit(self):
        pass

