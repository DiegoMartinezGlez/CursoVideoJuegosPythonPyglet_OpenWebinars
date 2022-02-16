import pyglet
from pyglet.window import key
from config import *
from ball import Ball
from platform import Platform


JOYSTICK_ON = False
joysticks = pyglet.input.get_joysticks()
if joysticks:
    joystick = joysticks[0]
    joystick.open()
    JOYSTICK_ON = True


window  = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "2D Game Engine Sandbox", resizable=False, fullscreen=True)

batch = pyglet.graphics.Batch()

ball    = Ball(WINDOW_WIDTH//2, 0+BALL_RADIUS, BALL_RADIUS)

platforms = [
    Platform(WINDOW_WIDTH//4 - WINDOW_WIDTH//16,300, WINDOW_WIDTH//8, PLAT_WIDTH,(255, 255, 255), batch),
    Platform(3*WINDOW_WIDTH//4 - WINDOW_WIDTH//16,300, WINDOW_WIDTH//8, PLAT_WIDTH,(255, 255, 255), batch),
]

@window.event
def on_draw():
    window.clear()
    batch.draw()
    ball.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        ball.jump()
    if symbol == key.A:
        ball.do_left()
    if symbol == key.D:
        ball.do_right()

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.SPACE:
        ball.stop_jump()
    if symbol == key.A:
        ball.stop_left()
    if symbol == key.D:
        ball.stop_right()

if JOYSTICK_ON:
    @joystick.event
    def on_joyhat_motion(joystick, hat_x, hat_y):
        # handle just right and left
        if hat_x == -1:
            ball.do_left()
        if hat_x == 1:
            ball.do_right()
        if hat_x == 0:
            ball.stop_left()
            ball.stop_right()

    @joystick.event
    def on_joybutton_press(joystick, button):
        #print("button pressed:", button)

        # X button: jump!
        if button == 0:
            ball.jump()

    @joystick.event
    def on_joybutton_release(joystick, button):
        #print("button released:", button)
        pass

    '''
    @joystick.event
    def on_joyaxis_motion(joystick, axis, value):
        print("on_joyaxis_motion")
        print("axis", axis)
        print("value", value)
        if axis == "x" and value>0.2:            
            ball.do_right()
            ball.stop_left()
        elif axis == "x" and value<-0.2:
            ball.do_left()
            ball.stop_right()
    '''
            


def update(dt):
    ball.update(dt)
    checkCollisions()

def checkCollisions():
    # floor collision
    if ball.circle.y-ball.width<0:
        ball.vel_y = 0.0
        ball.circle.y = ball.width
        ball.state_y = PLAYER_STATE_IDLE
    
    # walls collision (left&right screen borders)
    ball.on_wall = False
    if ball.circle.x-ball.width<MAGNET_WALLS:
        if ball.state_x != PLAYER_STATE_RIGHT:
            ball.vel_x = 0.0
            ball.circle.x = ball.width
            ball.state_x = PLAYER_STATE_IDLE
            ball.on_wall = True
            #ball.stop_jump()

    if ball.circle.x+ball.width>WINDOW_WIDTH-MAGNET_WALLS:
        if ball.state_x != PLAYER_STATE_LEFT:
            ball.vel_x = 0.0
            ball.circle.x = WINDOW_WIDTH-ball.width
            ball.state_x = PLAYER_STATE_IDLE
            ball.on_wall = True
            #ball.stop_jump()
    
    # platforms collisions
    if ball.vel_y<0: # if ball is falling down
        for plat in platforms:
            if plat.contains(ball.circle.x, ball.circle.y-ball.width):
                ball.vel_y = 0.0
                ball.state_y = PLAYER_STATE_IDLE
                ball.circle.y = plat.rect.y + plat.rect.height + ball.width
                
            
        
            
        



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()





# TODO: platforms
# TODO: double jump
# TODO: impulse from point direction function for ball class
