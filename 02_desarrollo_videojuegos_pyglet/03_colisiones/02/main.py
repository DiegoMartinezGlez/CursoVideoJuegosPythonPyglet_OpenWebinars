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
    Platform(0,0, WINDOW_WIDTH, PLAT_WIDTH),
    Platform(0,0, PLAT_WIDTH, WINDOW_HEIGHT),
    Platform(0,WINDOW_HEIGHT-PLAT_WIDTH, WINDOW_WIDTH, PLAT_WIDTH),
    Platform(WINDOW_WIDTH-PLAT_WIDTH,0, PLAT_WIDTH, WINDOW_HEIGHT),
    
    Platform(WINDOW_WIDTH//4 - WINDOW_WIDTH//16,300, WINDOW_WIDTH//8, PLAT_WIDTH),
    Platform(3*WINDOW_WIDTH//4 - WINDOW_WIDTH//16,300, WINDOW_WIDTH//8, PLAT_WIDTH),
]

@window.event
def on_draw():
    window.clear()
    for p in platforms:
        p.draw()
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

    # check collisions
    player.clearCollisionsFlags()
    if player.moving():
        for platf in platforms:

            # from up
            if player.movingUp() and (platf.contains(player.getTopLeft()[0], player.getTopLeft()[1]+player.speed) or platf.contains(player.getTopRight()[0], player.getTopRight()[1]+player.speed)):
                player.col_up = True
                player.rect.y = platf.rect.y - player.rect.height

            # from down

            if player.movingDown() and (platf.contains(player.getBtmLeft()[0], player.getBtmLeft()[1]-player.speed) or platf.contains(player.getBtmRight()[0], player.getBtmRight()[1]-player.speed)):
                player.col_down = True
                player.rect.y = platf.rect.height + platf.rect.y

            # from left
            if platf.contains(player.getTopLeft()[0]-player.speed, player.getTopLeft()[1]) or platf.contains(player.getBtmLeft()[0]-player.speed, player.getBtmLeft()[1]):
                player.col_left = True
                player.rect.x = platf.rect.width + platf.rect.x

           # from right
            if platf.contains(player.getTopRight()[0]+player.speed, player.getTopRight()[1]) or platf.contains(player.getBtmRight()[0]+player.speed, player.getBtmRight()[1]):
                player.col_right = True
                player.rect.x = platf.rect.x - player.rect.width

    player.move()



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
