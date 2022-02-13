import pyglet

window = pyglet.window.Window(960, 540)

label   = pyglet.text.Label('Hello, world',
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')

width   = 500
height  = 120
square  = pyglet.shapes.Rectangle(window.width//2 - width//2, window.height//2 - height//2, width, height, color=(185, 155, 55))

@window.event
def on_draw():
    window.clear()
    square.draw()
    label.draw()

pyglet.app.run()
