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

@window.event       
def on_key_press(symbol, modifiers):
    print('key press: ', symbol)

@window.event
def on_mouse_press(x, y, button, modifiers):
    print('mouse click press')

@window.event
def on_mouse_release(x, y, button, modifiers):
    print('mouse click release')

@window.event
def on_mouse_motion(x, y, dx, dy):
    pass

pyglet.app.run()
