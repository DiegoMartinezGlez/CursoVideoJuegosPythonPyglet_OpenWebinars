import pyglet
from pyglet.window import key

# constants
WINDOW_WIDTH    = 1280
WINDOW_HEIGHT   = 720

window  = pyglet.window.Window(1280, 720, "Pyglet Experiments", resizable=False)
pyglet.gl.glClearColor(*(255, 255, 255, 255))

batch   = pyglet.graphics.Batch()
rect01  = pyglet.shapes.Rectangle(window.width//2 - 50, window.height//8 - 10, 20, 20, color=(0, 0, 0), batch=batch)
rect_x_move = 'IDLE'
rect_left   = False
rect_right  = False
rect_speed  = 5

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    global rect_left, rect_right
    if symbol == key.A:
        rect_left = True
    if symbol == key.D:
        rect_right  = True

@window.event
def on_key_release(symbol, modifiers):
    global rect_left, rect_right
    if symbol == key.A:
        rect_left = False
    if symbol == key.D:
        rect_right  = False

def update(dt):
    global rect_x_move, rect_left, rect_right
    if (rect_left and rect_right) or (not rect_left and not rect_right):
        rect_x_move = 'IDLE'
    else:
        if rect_left:
            rect_x_move = 'LEFT'
        if rect_right:
            rect_x_move = 'RIGHT'
    
    if rect_x_move == 'LEFT':
        rect01.x -= rect_speed
    if rect_x_move == 'RIGHT':
        rect01.x += rect_speed


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
