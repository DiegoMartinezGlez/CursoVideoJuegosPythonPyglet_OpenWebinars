from brick import Brick
from config import *

class Block:
    def __init__(self, x, y, type): #, type):
        self.type           = type
        self.bricks         = []
        self.x              = x
        self.y              = y
        self.state          = 0

        if type == BLOCK_TYPE_I:
            self.type_i( x, y)
        elif type == BLOCK_TYPE_O:
            self.type_o( x, y)
        elif type == BLOCK_TYPE_T:
            self.type_t( x, y)
        elif type == BLOCK_TYPE_L:
            self.type_l( x, y)
        elif type == BLOCK_TYPE_J:
            self.type_j( x, y)
        elif type == BLOCK_TYPE_S:
            self.type_s( x, y)
        elif type == BLOCK_TYPE_Z:
            self.type_z( x, y)

    def type_o(self, x, y):
        self.color = (180, 0, 0)
        self.bricks.append(Brick(x, y, self.color))
        self.bricks.append(Brick(x+1, y, self.color))
        self.bricks.append(Brick(x, y-1, self.color))
        self.bricks.append(Brick(x+1, y-1, self.color))        

    # line blocks methods

    def type_i(self, x, y):
        self.color = (0, 0, 0)
        self.bricks = self.i_rotation_0(x, y)
    
    def i_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x+2, y, self.color))
        bricks.append(Brick(x-1, y, self.color))
        return bricks

    def i_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x, y+2, self.color))
        bricks.append(Brick(x, y-1, self.color))
        return bricks

    # t blocks methods

    def type_t(self, x, y):
        self.color = (80, 220, 80)
        self.bricks = self.t_rotation_0(x, y)

    def t_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        return bricks

    def t_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x-1, y, self.color))
        return bricks

    def t_rotation_2(self, x, y):
        bricks = []
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x, y+1, self.color))
        return bricks

    def t_rotation_3(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x+1, y, self.color))
        return bricks

    # l1 blocks methods

    def type_l(self, x, y):
        self.color = (0, 180, 0)
        self.bricks = self.l_rotation_0( x, y)
        
    def l_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x-1, y-1, self.color))
        return bricks

    def l_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x-1, y+1, self.color))
        return bricks

    def l_rotation_2(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x+1, y+1, self.color))
        return bricks

    def l_rotation_3(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x+1, y-1, self.color))
        return bricks

    # J blocks methods

    def type_j(self, x, y):
        self.color = (0, 0, 180)
        self.bricks = self.j_rotation_0(x, y)

    def j_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x-1, y-1, self.color))
        bricks.append(Brick(x+1, y-1, self.color))
        bricks.append(Brick(x-1, y, self.color))
        return bricks

    def j_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x+1, y+1, self.color))
        return bricks

    def j_rotation_2(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x+1, y-1, self.color))
        return bricks

    def j_rotation_3(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x-1, y-1, self.color))
        return bricks
        
    # s blocks methods

    def type_s(self, x, y):
        self.color = (220, 0, 180)
        self.bricks = self.s_rotation_0(x, y)

    def s_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x-1, y-1, self.color))
        return bricks

    def s_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y+1, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x+1, y-1, self.color))
        return bricks

    
    # z blocks methods
    
    def type_z(self, x, y):
        self.color = (220, 180, 0)
        self.bricks = self.z_rotation_0(x, y)

    def z_rotation_0(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x-1, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x+1, y-1, self.color))
        return bricks

    def z_rotation_1(self, x, y):
        bricks = []
        bricks.append(Brick(x, y, self.color))
        bricks.append(Brick(x, y-1, self.color))
        bricks.append(Brick(x+1, y, self.color))
        bricks.append(Brick(x+1, y+1, self.color))
        return bricks




    def move_right(self):
        self.x = self.x+1
        for brick in self.bricks:
            brick.move_right()

    def move_left(self):
        self.x = self.x-1
        for brick in self.bricks:
            brick.move_left()

    def move_down(self):
        self.y = self.y-1
        for brick in self.bricks:
            brick.move_down()

    def next_rotation(self):
        if self.type == BLOCK_TYPE_I:
            if self.state in (0,2):
                return self.i_rotation_1(self.x, self.y)
            else:
                return self.i_rotation_0(self.x, self.y)

        if self.type == BLOCK_TYPE_T:
            if self.state == 0:
                return self.t_rotation_1(self.x, self.y)
            elif self.state == 1:
                return self.t_rotation_2(self.x, self.y)
            elif self.state == 2:
                return self.t_rotation_3(self.x, self.y)
            elif self.state == 3:
                return self.t_rotation_0(self.x, self.y)

        if self.type == BLOCK_TYPE_L:
            if self.state == 0:
                return self.l_rotation_1(self.x, self.y)
            elif self.state == 1:
                return self.l_rotation_2(self.x, self.y)
            elif self.state == 2:
                return self.l_rotation_3(self.x, self.y)
            elif self.state == 3:
                return self.l_rotation_0(self.x, self.y)

        if self.type == BLOCK_TYPE_J:
            if self.state == 0:
                return self.j_rotation_1(self.x, self.y)
            elif self.state == 1:
                return self.j_rotation_2(self.x, self.y)
            elif self.state == 2:
                return self.j_rotation_3(self.x, self.y)
            elif self.state == 3:
                return self.j_rotation_0(self.x, self.y)

        if self.type == BLOCK_TYPE_S:
            if self.state in (0,2):
                return self.s_rotation_1(self.x, self.y)
            elif self.state in (1,3):
                return self.s_rotation_0(self.x, self.y)

        if self.type == BLOCK_TYPE_Z:
            if self.state in (0,2):
                return self.z_rotation_1(self.x, self.y)
            elif self.state in (1,3):
                return self.z_rotation_0(self.x, self.y)

        # default return, for square blocks
        return []


    def rotate(self, bricks):
        self.state = self.state+1
        if self.state == 4:
            self.state = 0

        if self.type != BLOCK_TYPE_O:
            self.bricks = bricks

