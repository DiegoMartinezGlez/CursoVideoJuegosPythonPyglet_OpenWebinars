import pyglet
from pyglet.window import key
import config

class Scene():
    def __init__(self, manager, id):
        self.manager    = manager
        self.id         = id
        self.batch      = pyglet.graphics.Batch()

    def on_draw(self):
        self.manager.window.clear()
        self.batch.draw()

    def loadScene(self):
        self.manager.window.set_caption("Scene "+str(self.id))
        self.title = pyglet.text.Label("Scene "+str(self.id), font_size=20, x=config.WINDOW_WIDTH//2, y=config.WINDOW_HEIGHT-60, batch=self.batch,
                        anchor_x ='center', anchor_y ='center')

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, buttons, modifiers):
        pass

    def exit(self):
        self.title.delete()
        pass

    def update(self, dt):
        pass


