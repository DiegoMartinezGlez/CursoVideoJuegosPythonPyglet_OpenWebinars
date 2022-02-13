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
        if self.y_state == STATE_GO_DOWN:
            self.rect.y -= self.speed
        if self.y_state == STATE_GO_UP:
            self.rect.y += self.speed

        if self.x_state == STATE_GO_LEFT:
            self.rect.x -= self.speed
        if self.x_state == STATE_GO_RIGHT:
            self.rect.x += self.speed
