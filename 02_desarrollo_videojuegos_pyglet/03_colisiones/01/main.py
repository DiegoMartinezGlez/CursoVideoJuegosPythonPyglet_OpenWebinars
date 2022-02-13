import pyglet
from pyglet.window import key
from player import Player
from platform import Platform

# constants
WINDOW_WIDTH    = 1280
WINDOW_HEIGHT   = 720
PLAT_WIDTH      = 30


window  = pyglet.window.Window(1280, 720, "Pyglet Experiments", resizable=False)
pyglet.gl.glClearColor(*(255, 255, 255, 255))

player  = Player(window, window.width//2, window.height//2)

platforms = [
    Platform(0,0, WINDOW_WIDTH, PLAT_WIDTH, batch),
    Platform(0,0, PLAT_WIDTH, WINDOW_HEIGHT, batch),
    Platform(0,WINDOW_HEIGHT-PLAT_WIDTH, WINDOW_WIDTH, PLAT_WIDTH, batch),
    Platform(WINDOW_WIDTH-PLAT_WIDTH,0, PLAT_WIDTH, WINDOW_HEIGHT, batch)
]

@window.event
def on_draw():
    window.clear()
    batch.draw()
    player.draw()

@window.event
def on_key_press(symbol, modifiers):
    global player
    if symbol == key.A:
        player.go_left = True
    if symbol == key.D:
        player.go_right  = True
    if symbol == key.W:
        player.go_up = True
    if symbol == key.S:
        player.go_down  = True

@window.event
def on_key_release(symbol, modifiers):
    global player
    if symbol == key.A:
        player.go_left = False
    if symbol == key.D:
        player.go_right  = False
    if symbol == key.W:
        player.go_up = False
    if symbol == key.S:
        player.go_down  = False

def update(dt):
    global player
    player.update(dt)
    player.move()
   


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
