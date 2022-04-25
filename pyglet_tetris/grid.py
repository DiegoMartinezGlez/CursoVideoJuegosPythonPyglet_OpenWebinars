import pyglet
from config import *
from block import Block
from next import Next
from help import Help
from score import Score
import random
import numpy as np

class Grid:
    def __init__(self, window):
        self.window         = window
        self.width          = 10            # in bricks
        self.height         = 24            # in bricks
        self.batch          = pyglet.graphics.Batch()

        self.next_panel     = Next(BRICK_WIDTH, self.window.height-BRICK_WIDTH*2)
        self.score_panel    = Score(BRICK_WIDTH, self.window.height-7.5*BRICK_WIDTH)
        self.help_panel     = Help(self.window.width-PANELS_WIDTH, self.window.height-BRICK_WIDTH*2)

        self.inner_offset   = 1
        self.base_bricks    = []
        self.current_block  = None
        self.blocks_bag     = []
        self.new_blocks_bag()
        self.blocks_counter = 0

        self.base_color     = BG_COLOR_DARK
        self.inner_color    = BG_COLOR

        self.topleft_x      = window.width//2 - self.width*BRICK_WIDTH//2
        self.topleft_y      = window.height//2 - self.height*BRICK_WIDTH//2

        for x in range(0, self.width):
            for y in range(0, self.height):
                posx = self.topleft_x + BRICK_WIDTH*x
                posy = self.topleft_y + BRICK_WIDTH*y
                self.base_bricks.append(
                    pyglet.shapes.Rectangle(posx, posy, BRICK_WIDTH, BRICK_WIDTH, color=self.base_color, batch=self.batch)
                )
                self.base_bricks.append(
                    pyglet.shapes.Rectangle(posx+self.inner_offset, posy+self.inner_offset, BRICK_WIDTH-self.inner_offset*2, BRICK_WIDTH-self.inner_offset*2, color=self.inner_color, batch=self.batch)
                )

        self.init_x         = 4
        self.init_y         = self.height-1
        posx = self.topleft_x + BRICK_WIDTH*self.init_x
        posy = self.topleft_y + BRICK_WIDTH*self.init_y
        
        self.new_game()

    def new_game(self):
        self.grid_content   = np.array( [ [None]*self.width for _ in range(self.height)] )
        self.new_block()

    def draw(self):
        # draw background base grid
        self.batch.draw()
                
        # draw current block bricks
        for brick in self.current_block.bricks:
            brick.rect.x = self.topleft_x + brick.x*BRICK_WIDTH
            brick.rect.y = self.topleft_y + brick.y*BRICK_WIDTH
            brick.rect.draw()
        # draw frozen bricks in self.grid_content
        for y in range(0, len(self.grid_content)):
            for x in range(0, len(self.grid_content[0])):
                brick = self.grid_content[y][x]
                if brick is not None:
                    brick.rect.x = self.topleft_x + brick.x*BRICK_WIDTH
                    brick.rect.y = self.topleft_y + brick.y*BRICK_WIDTH
                    brick.rect.draw()
        self.next_panel.draw()
        self.score_panel.draw()
        self.help_panel.draw()
        '''
        if self.next_panel.block is not None:
            for brick in self.next_panel.block.bricks:
                brick.rect.x = self.next_panel.x + brick.x*BRICK_WIDTH
                brick.rect.y = self.next_panel.y + brick.y*BRICK_WIDTH
                brick.rect.draw()
        '''

    # generates new blocks
    def new_block(self):
        self.current_block = Block(self.init_x, self.init_y, self.blocks_bag.pop(0))
        if len(self.blocks_bag) == 0:
            self.new_blocks_bag()
        self.next_panel.set_next(self.blocks_bag[0])
        # update score
        self.blocks_counter = self.blocks_counter+1
        self.score_panel.update_blocks(self.blocks_counter)
    
    def new_blocks_bag(self):
        self.blocks_bag = BLOCK_TYPES.copy()
        random.shuffle(self.blocks_bag)

    def move_block_right(self):
        if self.can_go_right():
            self.current_block.move_right()
            # if cannot go down, freeze block bricks
            if not self.can_go_down():
                for brick in self.current_block.bricks:
                    self.grid_content[brick.y][brick.x] = brick
                self.new_block()

    def can_go_right(self):
        for brick in self.current_block.bricks:
            if brick.x+1>=self.width:
                return False
            brick_on_right = self.grid_content[brick.y][brick.x+1]
            if brick_on_right is not None:
                return False
        return True

    def move_block_left(self):
        if self.can_go_left():
            self.current_block.move_left()
            # if cannot go down, freeze block bricks
            if not self.can_go_down():
                for brick in self.current_block.bricks:
                    self.grid_content[brick.y][brick.x] = brick
                self.new_block()
    
    def can_go_left(self):
        for brick in self.current_block.bricks:
            if brick.x-1<0:
                return False
            brick_on_left = self.grid_content[brick.y][brick.x-1]
            if brick_on_left is not None:
                return False
        return True

    def move_block_down(self):
        if self.can_go_down():
            self.current_block.move_down()
        else:
            # if the block cannot move, GAME OVER!
            if self.current_block.y >= self.init_y:
                self.window.game_over()
            else: # if cannot go down, FREEZE block bricks
                self.freeze()

    # gets the bricks of the current block and fix them in the grid
    def freeze(self):
        for brick in self.current_block.bricks:
            self.grid_content[brick.y][brick.x] = brick
        self.check_full_rows()
        self.new_block()
    
    # checks if any row is already full, called from "freeze" method
    def check_full_rows(self):
        lines_ids = []        
        for y in range(0, self.height):
            line_full = True
            for x in range(0, self.width):
                if self.grid_content[y][x] == None:
                    line_full = False
                    break
            if line_full:
                lines_ids.append(y)

        # if there was lines to be removed, manage row/s removal and shifting
        if len(lines_ids)>0:
            new_grid_content = []
            rows_removed = 0
            for y in range(0, self.height):
                if y in lines_ids:
                    rows_removed = rows_removed+1
                else:
                    row = self.grid_content[y]
                    new_grid_content.append(self.row_down(row, rows_removed))
            for i in range(0, rows_removed):
                new_grid_content.append([None,None,None,None,None,None,None,None,None,None])
            self.grid_content = new_grid_content
        
            # update score
            self.score_panel.update_lines(len(lines_ids))

    # this method updates bricks coordinates for shifted rows, used as helper in "check_full_lines" method
    def row_down(self, row, num):
        for brick in row:
            if brick is not None:
                brick.y = brick.y-num
        return row

    def can_go_down(self):
        for brick in self.current_block.bricks:
            if brick.y-1<0:
                return False
            brick_below = self.grid_content[brick.y-1][brick.x]
            if brick_below is not None:
                return False
        return True

    def can_rotate(self):
        rotated_bricks = self.current_block.next_rotation()
        for brick in rotated_bricks:
            if brick.x<0 or brick.x>=self.width or brick.y<0 or brick.y>=self.height:
                return False
            brick_below = self.grid_content[brick.y][brick.x]
            if brick_below is not None:
                return False
        return True

    def rotate_block(self):
        if self.can_rotate():
            self.current_block.rotate(self.current_block.next_rotation())
