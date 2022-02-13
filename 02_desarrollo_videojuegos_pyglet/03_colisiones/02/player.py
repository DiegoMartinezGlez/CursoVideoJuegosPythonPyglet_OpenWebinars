import pyglet

STATE_IDLE      = 0
STATE_GO_LEFT   = 1
STATE_GO_RIGHT  = 2
STATE_GO_UP     = 3
STATE_GO_DOWN   = 4

class Player():
    def __init__(self, window, x, y):
        self.window     = window
        self.width      = 20
        self.batch      = pyglet.graphics.Batch()
        self.rect       = pyglet.shapes.Rectangle(x, y, self.width, self.width, color=(0, 0, 0), batch=self.batch)
        
        # movement variables
        self.x_state    = STATE_IDLE
        self.y_state    = STATE_IDLE
        self.go_left    = False
        self.go_right   = False
        self.go_up      = False
        self.go_down    = False
        self.speed      = 5

        # collision flags
        self.col_left   = False
        self.col_right  = False
        self.col_up     = False
        self.col_down   = False



    def draw(self):
        self.batch.draw()

    def update(self, dt):
        if (self.go_left and self.go_right) or (not self.go_left and not self.go_right):
            self.x_state = STATE_IDLE
        else:
            if self.go_left:
                self.x_state = STATE_GO_LEFT
            if self.go_right:
                self.x_state = STATE_GO_RIGHT

        if (self.go_up and self.go_down) or (not self.go_up and not self.go_down):
            self.y_state = STATE_IDLE
        else:
            if self.go_up:
                self.y_state = STATE_GO_UP
            if self.go_down:
                self.y_state = STATE_GO_DOWN
        
    def move(self):
        if self.y_state == STATE_GO_DOWN and not self.col_down:
            self.rect.y -= self.speed
        if self.y_state == STATE_GO_UP and not self.col_up:
            self.rect.y += self.speed

        if self.x_state == STATE_GO_LEFT and not self.col_left:
            self.rect.x -= self.speed
        if self.x_state == STATE_GO_RIGHT and not self.col_right:
            self.rect.x += self.speed
    
    def getTopLeft(self):
        return (self.rect.x, self.rect.y + self.rect.height)
    def getTopRight(self):
        return (self.rect.x+self.rect.width, self.rect.y + self.rect.height)
    def getBtmLeft(self):
        return (self.rect.x, self.rect.y)
    def getBtmRight(self):
        return (self.rect.x+self.rect.width, self.rect.y)

    def clearCollisionsFlags(self):
        self.col_left   = False
        self.col_right  = False
        self.col_up     = False
        self.col_down   = False

    def moving(self):
        if self.y_state != STATE_IDLE or self.x_state != STATE_IDLE:
            return True
        return False
    
    def movingUp(self):
        return self.y_state == STATE_GO_UP
    def movingDown(self):
        return self.y_state == STATE_GO_DOWN
    def movingLeft(self):
        return self.x_state == STATE_GO_LEFT
    def movingRight(self):
        return self.x_state == STATE_GO_RIGHT



