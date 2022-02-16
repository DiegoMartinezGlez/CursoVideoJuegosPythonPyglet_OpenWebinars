import pyglet
import random
from config import *
import time

class Ball():
    def __init__(self, x, y, width):
        self.width          = width
        self.state_y        = PLAYER_STATE_IDLE
        self.state_x        = PLAYER_STATE_IDLE
        self.on_wall        = False
        self.vel_x          = 0.0
        self.vel_y          = 0.0
        self.vel_y_top      = 4.5
        self.gravity        = 10.0
        self.delta_factor   = 140
        self.jump_imp       = 20.0
        self.jump_imp_fst   = 60.0
        self.walk_imp       = 4.0
        self.start_jump     = 0.0
        self.jump_time_top  = 0.2
        self.acc_y          = 0.0
        self.do_jump        = False
        self.go_left        = False
        self.go_right       = False
        self.circle         = pyglet.shapes.Circle(x, y, self.width, color=COLOR_BLUE)

        self.label          = pyglet.text.Label('',
                                                font_size=18,
                                                x= WINDOW_WIDTH // 8,
                                                y= 6.5*WINDOW_HEIGHT // 8,
                                                anchor_x='left',
                                                anchor_y='center')

        self.label2         = pyglet.text.Label('',
                                                font_size=18,
                                                x= WINDOW_WIDTH // 8,
                                                y= 7*WINDOW_HEIGHT // 8,
                                                anchor_x='left',
                                                anchor_y='center')
    
        self.label3         = pyglet.text.Label('',
                                                font_size=18,
                                                x= WINDOW_WIDTH // 8,
                                                y= 7.5*WINDOW_HEIGHT // 8,
                                                anchor_x='left',
                                                anchor_y='center')

    def draw(self):
        self.circle.draw()
        self.label.draw()
        self.label2.draw()
        self.label3.draw()

    def update(self, dt):

        # y        
        if self.do_jump == True and self.state_y != PLAYER_STATE_JUMP:
            self.state_y = PLAYER_STATE_JUMP
            self.start_jump = time.time()
            #if DEBUG: print("new start jump time: ", self.start_jump)

        if self.state_y == PLAYER_STATE_JUMP and self.on_wall:
            self.state_y = PLAYER_STATE_WIDLE
        if self.state_y == PLAYER_STATE_WIDLE and not self.on_wall:
            self.state_y = PLAYER_STATE_JUMP

        if self.state_y == PLAYER_STATE_JUMP:
            current_time = time.time()
            jump_time = current_time - self.start_jump
            jump_time = round(jump_time*10)/10
            #if DEBUG: print("jump_time", jump_time) 

        self.vel_y = self.vel_y + self.accelerations()*dt
        if abs(self.vel_y)>self.vel_y_top:
            self.vel_y = self.vel_y_top*(self.vel_y/abs(self.vel_y))
        if self.on_wall and self.vel_y>0:
            self.vel_y=0

        # x
        # if not walking, stop with inertia
        if abs(self.vel_x)>0.0:
            if self.state_y == PLAYER_STATE_JUMP:
                self.vel_x = self.vel_x/1.05
            else:
                self.vel_x = self.vel_x/1.15
        if abs(self.vel_x)<0.5:
            self.vel_x = 0.0
        # handle left/right impulse, or idle
        if not self.go_left or not self.go_right:
            if self.go_left == True:
                self.vel_x = -self.walk_imp
                self.state_x = PLAYER_STATE_LEFT
            if self.go_right == True:
                self.vel_x = self.walk_imp
                self.state_x = PLAYER_STATE_RIGHT
        if not self.go_left and not self.go_right:
            self.state_x = PLAYER_STATE_IDLE


        # move
        self.circle.x   += self.vel_x*dt*self.delta_factor
        # TODO: to reduce x move on jump, we have to state if x impulse was requested before or after the jump started
        if self.isAnchorOnWall():
            if self.canJump() and self.do_jump:
                self.circle.y   += self.vel_y*dt*self.delta_factor*1.5
        else:
            self.circle.y   += self.vel_y*dt*self.delta_factor*1.5

        # debug
        if DEBUG:
            self.label.text = ("vel_y : "+str(round(self.vel_y*10)/10) 
                                + " acc_y : "+str(round(self.acc_y))
                                + " state_y "+self.state_y)

            self.label2.text = ("vel_x : "+str(round(self.vel_x*10)/10) 
                                + " state_x "+self.state_x)
            
            self.label3.text = ("on_wall: "+str(self.on_wall))

    
    def do_left(self):
        self.go_left = True
    
    def do_right(self):
        self.go_right = True
    
    def stop_left(self):
        self.go_left = False
    
    def stop_right(self):
        self.go_right = False
    
    def jump(self):
        self.do_jump = True
    
    def stop_jump(self):
        self.do_jump = False

    def accelerations(self):
        
        gravity_final = self.gravity

        if self.on_wall:
            gravity_final = self.gravity/5
        if self.isAnchorOnWall():
            gravity_final = 0.0

        # by default, apply just gravity
        self.acc_y = -gravity_final

        if self.state_y == PLAYER_STATE_JUMP or self.state_y == PLAYER_STATE_WIDLE:
            if self.canJump():
                # if there was no previous impulse, aply first impulse
                if self.acc_y == -gravity_final: 
                    self.acc_y = -gravity_final + self.jump_imp_fst
                else:
                    self.acc_y = -gravity_final + self.jump_imp
                #if DEBUG: print("add jump impulse!")
            else:
                self.stop_jump()

        return self.acc_y

    def canJump(self):
        current_time = time.time()
        jump_time = current_time - self.start_jump
        jump_time = round(jump_time*100)/100
        return self.isAnchorOnWall() or self.do_jump == True and jump_time<self.jump_time_top

    def isAnchorOnWall(self):
        return self.on_wall and (self.state_x == PLAYER_STATE_LEFT or self.state_x == PLAYER_STATE_RIGHT)