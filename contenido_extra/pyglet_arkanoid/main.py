import pyglet
from pyglet.window import key
from config import *
from player import Player
from bounds import Bounds
from ball import Ball


window  = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Pyrkanoid", resizable=False, fullscreen=True)
# white color for background
pyglet.gl.glClearColor(*COLOR_WHITE2)

batch   = pyglet.graphics.Batch()

bounds  = Bounds(WINDOW_WIDTH//2)
player  = Player(WINDOW_WIDTH//2, PLAYER_POS_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
ball    = Ball(WINDOW_WIDTH//2, PLAYER_POS_Y+BALL_RADIUS, BALL_RADIUS)


@window.event
def on_draw():
    window.clear()
    batch.draw()
    bounds.draw()
    player.draw()
    ball.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A or symbol == key.LEFT:
        player.goLeft()
    if symbol == key.D or symbol == key.RIGHT:
        player.goRight()

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.A or symbol == key.LEFT:
        player.stopLeft()
    if symbol == key.D or symbol == key.RIGHT:
        player.stopRight()

def update(dt):
    ball.update(dt)
    player.update(dt)
    checkCollisions()

def checkCollisions():
    
    # player with bounds
    if not bounds.checkLeftSideIn(player.x):
        player.fix_x(bounds.getLeftX())
    if not bounds.checkRightSideIn(player.x+player.width):
        player.fix_x(bounds.getRightX()-player.width)

    # ball with player
    if (ball.circle.x-ball.width//2 >= player.x and 
        ball.circle.x+ball.width//2 <= player.x+player.width and
        ball.circle.y-ball.width//2 >= player.y and 
        ball.circle.y-ball.width//2 <= player.y+player.height):
        ball.circle.y = ball.circle.radius + player.y+player.height
        ball.reboundY(player.vel//8)


    # ball with bounds:
    if not bounds.checkLeftSideIn(ball.circle.x-ball.width//2):
        ball.circle.x = bounds.inner_rect.x + ball.circle.radius
        ball.reboundX()
    if not bounds.checkRightSideIn(ball.circle.x+ball.width//2):
        ball.circle.x = bounds.inner_rect.x + bounds.inner_rect.width - ball.circle.radius
        ball.reboundX()
    if not bounds.checkTopSideIn(ball.circle.y+ball.width//2):
        ball.circle.y = bounds.inner_rect.y + bounds.inner_rect.height - ball.circle.radius
        ball.reboundY(0.0)

    # ball out of screen
    if ball.circle.y < 0:
        # game over! exit game
        pyglet.app.exit()
    



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()
