import pyglet
from config import *



class Player():
    def __init__(self, x, y, width, height):    
        self.x              = x-width//2
        self.y              = y-height
        self.width          = width
        self.height         = height

        self.move_state     = MOVE_STATE_IDLE
        self.last_state     = MOVE_STATE_IDLE
        self.cmd_go_left    = False
        self.cmd_go_right   = False
        self.vel            = 0.0
        self.dx             = 0.0

        self.top_vel        = 80.0
        self.min_vel        = 2.0
        self.top_dx         = 2.0
        self.speed_factor   = 8
        self.impulse_factor = 200
        self.reduce_factor  = 10

        self.rect       = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=COLOR_BLACK)

        self.vel_label  = pyglet.text.Label("VEL: "+str(self.vel),
                            font_size=10,
                            color=COLOR_BLACK2,
                            x=self.x, y=40,
                            anchor_x='center', anchor_y='center')

        self.state_label = pyglet.text.Label("Sate: "+self.move_state,
                            font_size=10,
                            color=COLOR_BLACK2,
                            x=self.x, y=20,
                            anchor_x='center', anchor_y='center')

    def update(self, dt):

        # debug
        if DEBUG:
            self.state_label.text   = self.move_state
            self.vel_label.text     = "VEL: "+str(self.vel)

        # update impulse
        # impulse left
        impulse = dt*self.impulse_factor
        if self.cmd_go_left and not self.cmd_go_right:
            self.last_state     = self.move_state
            self.move_state     = MOVE_STATE_LEFT
            if self.last_state == MOVE_STATE_RIGHT:
                self.clearPushRadical()
            self.pushLeft(impulse)
        # impulse right
        elif not self.cmd_go_left and self.cmd_go_right:
            self.last_state     = self.move_state
            self.move_state     = MOVE_STATE_RIGHT
            if self.last_state == MOVE_STATE_LEFT:
                self.clearPushRadical()
            self.pushRight(impulse)
        # no impulse
        else:
            self.clearPush()
            if self.vel == 0.0:
                self.last_state     = self.move_state
                self.move_state     = MOVE_STATE_IDLE


        # update velocity and move
        self.update_vel()
        self.move(dt)

        if DEBUG:
            print(self.move_state)
            print(self.vel)
            print(self.dx)
        

    def draw(self):
        self.rect.draw()
        if DEBUG:
            self.vel_label.draw()
            self.state_label.draw()

    def goLeft(self):
        self.cmd_go_left    = True

    def goRight(self):
        self.cmd_go_right   = True

    def stopLeft(self):
        self.cmd_go_left    = False

    def stopRight(self):
        self.cmd_go_right   = False

    def pushLeft(self, impulse):
        self.dx -= impulse
        if abs(self.dx)>self.top_dx:
            self.dx = -self.top_dx

    def pushRight(self, impulse):
        self.dx += impulse
        if self.dx>self.top_dx:
            self.dx = self.top_dx

    def clearPushRadical(self):
        # set velocity to cero

        if abs(self.dx)>0.0:
            self.dx = 0.0
        if abs(self.vel)>0.0:
            self.vel = 0.0

    def clearPush(self):
        # reduce velocity until abs(self.vel)<self.min_vel
        # (simulates inertia)

        if abs(self.dx)>0.0:
            self.dx = 0.0

        if abs(self.vel)>0.0:
            if abs(self.vel)<self.min_vel:
                self.vel = 0.0
            else:
                if self.vel>0.0:
                    self.vel = self.vel - self.vel/self.reduce_factor

                elif self.vel<0.0:
                    self.vel = self.vel - self.vel/self.reduce_factor

    def move(self, dt):
        self.x += self.vel * dt * self.speed_factor
        self.rect.x = self.x

    def fix_x(self, new_x):
        self.x = new_x
        self.rect.x = self.x

    def update_vel(self):

        self.vel += self.dx

        if abs(self.vel)>self.top_vel:
            if self.vel>0:
                self.vel = self.top_vel
            elif self.vel<0:
                self.vel = -self.top_vel

        if abs(self.vel)<self.min_vel:
            self.vel = 0.0



