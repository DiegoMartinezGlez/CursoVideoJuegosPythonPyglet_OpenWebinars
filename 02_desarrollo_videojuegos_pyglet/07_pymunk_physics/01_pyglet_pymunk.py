import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import time


window = pyglet.window.Window(1280, 720, "Pyglet Pymunk Experiments", resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -500

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)




body = pymunk.Body(1, 100)
body.position = window.width/2, 3*window.height/4

poly = pymunk.Poly.create_box(body, size=(50, 50))

space.add(body, poly)






if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()