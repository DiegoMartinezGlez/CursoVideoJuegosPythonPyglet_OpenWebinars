import pyglet

window = pyglet.window.Window(960, 540)

batch = pyglet.graphics.Batch()

pyglet.font.add_file('retro.ttf')
retroFont = pyglet.font.load('retro.ttf', 16)


width   = 500
height  = 120
rect  = pyglet.shapes.Rectangle(window.width//2 - width//2, window.height//2 - height//2, width, height, color=(185, 155, 55))

label   = pyglet.text.Label('Hello, world',
                            font_name='Retro Computer',
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    rect.draw()
    label.draw()

pyglet.app.run()
