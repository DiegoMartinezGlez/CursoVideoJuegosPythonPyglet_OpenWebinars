import pyglet
from button import Button


pyglet.font.add_file('retro.ttf')
retroFont = pyglet.font.load('retro.ttf', 16)

window = pyglet.window.Window(960, 540)

btn  = Button(window.width//2, window.height//2, 100, 80, "OK")

@window.event
def on_draw():
    window.clear()
    btn.draw()

pyglet.app.run()
