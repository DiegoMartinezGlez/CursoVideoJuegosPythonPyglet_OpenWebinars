import pyglet
from pyglet.window import key

from player import Player
from platform import Platform

# constants
WINDOW_WIDTH    = 1280
WINDOW_HEIGHT   = 720
PLAT_WIDTH      = 30


window  = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Pyglet Experiments", resizable=False)
pyglet.gl.glClearColor(*(255, 255, 255, 255))

batch   = pyglet.graphics.Batch()
player  = Player(window, 100, 100)


p1      = Platform(200, 200, 100, 20, (80,80,80), batch)
p2      = Platform(400, 300, 100, 20, (80,80,80), batch)

platforms = [
    Platform(0,0, WINDOW_WIDTH, PLAT_WIDTH, (80,80,80), batch),
    Platform(0,100-PLAT_WIDTH, WINDOW_WIDTH, PLAT_WIDTH, (80,80,80), batch),
    Platform(0,0, PLAT_WIDTH, WINDOW_HEIGHT, (80,80,80), batch),
    Platform(0,WINDOW_HEIGHT-PLAT_WIDTH, WINDOW_WIDTH, PLAT_WIDTH, (80,80,80), batch),
    Platform(WINDOW_WIDTH-PLAT_WIDTH,0, PLAT_WIDTH, WINDOW_HEIGHT, (80,80,80), batch),
    p1, p2, ]




@window.event
def on_draw():
    window.clear()
    batch.draw()
    player.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        player.goLeft()
    if symbol == key.D:
        player.goRight()
    if symbol == key.W:
        player.jump()

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        player.stopLeft()
    if symbol == key.D:
        player.stopRight()
    if symbol == key.W:
        player.stopJumping()


def update(dt):


    player.update(dt)
    #player.move()
    checkCollisions()
    
def checkCollisions():
    # check player vs platforms
    player.clearCollisionsFlags()
    for platform in platforms:
        if platform.contains( player.btnPoint()[0], player.btnPoint()[1] ):
            player.collisionBtn = True
            player.collitionBtnTop = platform.rect.y + platform.rect.height
    








if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()

