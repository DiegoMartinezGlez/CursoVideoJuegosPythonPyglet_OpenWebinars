import pyglet
import config
from scene import Scene

class SceneManager():
    def __init__(self):
        self.window     = pyglet.window.Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "1", resizable=False)
        self.scenes     = [ Scene(self, 1), Scene(self, 2) ]
        self.current    = 0

    def start(self):
        self.scenes[self.current].loadScene()
        self.window.remove_handlers()
        self.window.set_handler("on_draw", self.scenes[self.current].on_draw)
        self.window.set_handler("on_key_press", self.scenes[self.current].on_key_press)

    def exit(self):
        pyglet.app.exit()

    def nextScene(self):
        self.scenes[self.current].exit()
        self.current += 1
        if self.current < len(self.scenes):
            self.start()
        else:
            self.exit()

