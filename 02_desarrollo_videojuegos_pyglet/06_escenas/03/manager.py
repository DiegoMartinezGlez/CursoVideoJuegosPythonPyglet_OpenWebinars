import pyglet
import config
from scene import Scene
from menu import Menu
from play import Play

class SceneManager():
    def __init__(self):
        self.window     = pyglet.window.Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "1", resizable=False)
        self.scenes     = [ Menu(self, 1), Play(self, 2) ]
        self.current    = 0

    def start(self):
        self.scenes[self.current].loadScene()
        self.window.remove_handlers()
        self.window.set_handler("on_draw", self.scenes[self.current].on_draw)
        self.window.set_handler("on_key_press", self.scenes[self.current].on_key_press)
        self.window.set_handler("on_key_release", self.scenes[self.current].on_key_release)
        self.window.set_handler("on_mouse_press", self.scenes[self.current].on_mouse_press)
        pyglet.clock.schedule_interval(self.scenes[self.current].update, 1.0/120)

    def exit(self):
        pyglet.app.exit()

    def nextScene(self):
        self.scenes[self.current].exit()
        self.current += 1
        if self.current < len(self.scenes):
            self.start()
        else:
            self.exit()
