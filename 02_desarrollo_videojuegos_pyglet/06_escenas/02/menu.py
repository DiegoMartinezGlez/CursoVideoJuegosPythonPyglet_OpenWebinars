import pyglet
from pyglet.window import key
import config
from scene import Scene
from button import Button

class Menu(Scene):
    def __init__(self, manager, id):
        self.manager    = manager
        self.id         = id
        self.batch      = pyglet.graphics.Batch()

    def on_draw(self):
        super().on_draw()
        self.btn.draw()

    def on_mouse_press(self, x, y, buttons, modifiers):
        print("menu on mouse press")
        play_action = self.btn.mousePress(x, y)
        if play_action == config.ACTION_PLAY:
            print("let's play!")
            self.manager.nextScene()            
        else:
            print("try again ...")

    def loadScene(self):
        self.manager.window.set_caption("Game Menu")
        self.title = pyglet.text.Label("Game Menu", font_size=20, x=config.WINDOW_WIDTH//2, y=config.WINDOW_HEIGHT-60, batch=self.batch,
                        anchor_x ='center', anchor_y ='center')
        self.btn    = Button(config.WINDOW_WIDTH//2, config.WINDOW_HEIGHT//2, "PLAY", config.ACTION_PLAY)

    def exit(self):
        self.title.delete()

