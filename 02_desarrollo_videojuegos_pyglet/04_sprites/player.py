import pyglet

X_STATE_IDLE    = "x_state_idle"
X_STATE_RIGHT   = "x_state_right"
X_STATE_LEFT    = "x_state_left"
Y_STATE_IDLE    = "y_state_idle"
Y_STATE_JUMP    = "y_state_jump"
Y_STATE_FALL    = "y_state_fall"

X_IMPULSE       = 10

VAL_X_TOP       = 5
VAL_X_TOP_JUMP  = 4
VAL_Y_TOP       = 200

VEL_X_MIN       = 0.005
VEL_Y_MIN       = 0.05

GRAVITY_FORCE   = 4
JUMP_IMPULSE    = 30



class Player():
    def __init__(self, window, x, y):
        self.window     = window
        self.batch      = pyglet.graphics.Batch()
        self.vel_x      = 0.0
        self.dx         = 0.0
        self.vel_y      = 0.0
        self.dy         = 0.0

        self.jumpImpulse = 0.0

        self.go_left    = False
        self.go_right   = False
        self.jumping    = False
        self.x_state    = X_STATE_IDLE
        self.x_last_state = X_STATE_RIGHT
        self.y_state    = Y_STATE_IDLE
        self.y_last_state    = Y_STATE_IDLE
        self.lookLeft   = False
        self.lookRight  = True

        self.collisionBtn   = False
        self.collisionTop   = False
        self.collisionLeft  = False
        self.collisionRight = False
        
        self.collitionBtnTop = None

        anim            = pyglet.image.load('player_48x64.png')
        anim_seq        = pyglet.image.ImageGrid(anim, 3, 4)
        self.sprite_grid = pyglet.image.TextureGrid(anim_seq)
        self.poseRef    = {"walk_left": [4.0,7.0], "walk_right": [8.0,11.0], "jump_left": [1.0,1.0], "jump_right": [0.0,0.0]}
        self.idFrame    = self.poseRef["walk_right"][0]
        self.sprite     = pyglet.sprite.Sprite(self.sprite_grid[int(self.idFrame)], x, y, batch = self.batch)

        self.btnRef     = pyglet.shapes.Rectangle(self.btnPoint()[0], self.btnPoint()[1], 10, 10, color = (150, 0, 0), batch = self.batch)

    def draw(self):
        self.sprite.draw()


    def update(self, dt):

        self.dx = 0.0
        inc_x = dt*X_IMPULSE
        if self.go_right:
            self.lookToRight()
            self.x_state = X_STATE_RIGHT
            self.dx = self.dx + inc_x
            if self.vel_x<0.0:
                self.vel_x = self.vel_x / 2
        elif self.go_left:
            self.lookToLeft()
            self.x_state = X_STATE_LEFT
            self.dx = self.dx - inc_x
            if self.vel_x>0.0:
                self.vel_x = self.vel_x / 2
        
        if self.dx == 0 and abs(self.vel_x)>0.0:
            self.vel_x = self.vel_x / 2
        else: 
            self.vel_x = self.vel_x + self.dx

        if abs(self.vel_x) > VAL_X_TOP:
            if self.lookRight:
                self.vel_x = VAL_X_TOP
            else:
                self.vel_x = -VAL_X_TOP
        if self.y_state == Y_STATE_FALL:
            if abs(self.vel_x) > VAL_X_TOP_JUMP:
                if self.lookRight:
                    self.vel_x = VAL_X_TOP_JUMP
                else:
                    self.vel_x = -VAL_X_TOP_JUMP

        self.dy = -GRAVITY_FORCE
        if self.y_state == Y_STATE_IDLE and self.jumpImpulse > 0.0:
            self.dy = self.dy + self.jumpImpulse

        self.jumpImpulse = 0.0
        
        self.vel_y =  self.vel_y + self.dy

        if self.vel_y >= VAL_Y_TOP:
            self.vel_y = VAL_Y_TOP
        if self.vel_y < -VAL_Y_TOP:
            self.vel_y = -VAL_Y_TOP
        
        self.move()

        if self.vel_y <= -GRAVITY_FORCE:
            self.vel_y = 0.0
        
        if abs(self.vel_y)<VEL_Y_MIN/2:
            self.vel_y = 0.0

        if abs(self.vel_x)<VEL_X_MIN/2:
            self.vel_x = 0
        
        if self.dy>-GRAVITY_FORCE:
            self.y_last_state = self.y_state
            self.y_state = Y_STATE_JUMP
            if self.y_last_state != self.y_state:

                if self.x_state == X_STATE_RIGHT:
                    self.idFrame = self.poseRef["walk_right"][0]
                if self.x_state == X_STATE_LEFT:
                    self.idFrame = self.poseRef["walk_left"][0]


        #elif self.sprite.y>100 and not self.collisionBtn:
        elif not self.collisionBtn:
            self.y_last_state = self.y_state
            self.y_state = Y_STATE_FALL
            if self.y_last_state != self.y_state:

                if self.x_state == X_STATE_RIGHT:
                    self.idFrame = self.poseRef["walk_right"][0]
                if self.x_state == X_STATE_LEFT:
                    self.idFrame = self.poseRef["walk_left"][0]


        else:
            if self.y_last_state != self.y_state:

                if self.x_state == X_STATE_RIGHT:
                    self.idFrame = self.poseRef["walk_right"][0]
                if self.x_state == X_STATE_LEFT:
                    self.idFrame = self.poseRef["walk_left"][0]

            self.y_last_state = self.y_state
            self.y_state = Y_STATE_IDLE


        # calculate sprite frame
        if self.moving():
            self.nextFrame()
        else:
            
            if self.x_state == X_STATE_RIGHT:
                self.idFrame = self.poseRef["walk_right"][0]
            if self.x_state == X_STATE_LEFT:
                self.idFrame = self.poseRef["walk_left"][0]
            
        if int(self.idFrame)<len(self.sprite_grid):
            current_frame = self.sprite_grid[int(self.idFrame)].get_texture()
            self.sprite._set_texture(current_frame)


    def move(self):
        print('move')
        print('self.vel_y', self.vel_y)
        self.sprite.x   += self.vel_x*2
        if self.vel_y>0 or (self.vel_y < 0 and not self.collisionBtn):
            self.sprite.y   += self.vel_y*2
        if self.vel_y <= 0 and self.collisionBtn and self.collitionBtnTop!=None:
            self.sprite.y = self.collitionBtnTop
            self.collitionBtnTop = None
        if self.sprite.x<0:
            self.sprite.x = 0
        if self.sprite.x + self.sprite.width > self.window.width:
            self.sprite.x = self.window.width - self.sprite.width

        btnPnt = self.btnPoint()
        self.btnRef.x = btnPnt[0]
        self.btnRef.y = btnPnt[1]

    def moving(self):
        if abs(self.vel_x)>0.0 or self.vel_y!=0:
            return True
        else:
            return False

    def nextFrame(self):

        # roll frame only if there is x-axis movement
        if abs(self.vel_x)>0.0:
            self.idFrame = self.idFrame+0.3

        if self.y_state == Y_STATE_IDLE:
            #if self.x_state!=self.x_last_state and self.x_state == X_STATE_RIGHT:
            if self.x_state == X_STATE_RIGHT:
                if self.idFrame > self.poseRef["walk_right"][1]+1:
                    self.idFrame = self.poseRef["walk_right"][0]
            #if self.x_state!=self.x_last_state and self.x_state == X_STATE_LEFT:
            if self.x_state == X_STATE_LEFT:
                if self.idFrame > self.poseRef["walk_left"][1]+1:
                    self.idFrame = self.poseRef["walk_left"][0]
        elif self.y_state == Y_STATE_JUMP or self.y_state == Y_STATE_FALL:
            if self.lookRight:
                if self.idFrame >= self.poseRef["jump_right"][1]+1:
                    self.idFrame = self.poseRef["jump_right"][0]
            if self.lookLeft:
                if self.idFrame >= self.poseRef["jump_left"][1]+1:
                    self.idFrame = self.poseRef["jump_left"][0]

    def goLeft(self):
        self.go_left = True

    def goRight(self):
        self.go_right = True

    def stopLeft(self):
        self.go_left = False

    def stopRight(self):
        self.go_right = False

    def jump(self):
        if not self.jumping:
            self.jumpImpulse = JUMP_IMPULSE
        self.jumping = True

    def stopJumping(self):
        self.jumping = False

    def lookToLeft(self):
        self.lookLeft   = True
        self.lookRight  = False

    def lookToRight(self):
        self.lookLeft   = False
        self.lookRight  = True

    # ref points methods
    def btnPoint(self):
        x = self.sprite.x + self.sprite.width/2
        y = self.sprite.y
        return (x, y)


    def clearCollisionsFlags(self):
        self.collisionBtn   = False
        self.collisionTop   = False
        self.collisionLeft  = False
        self.collisionRight = False
