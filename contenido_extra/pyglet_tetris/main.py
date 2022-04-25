import pyglet
from grid import Grid
from config import *

key = pyglet.window.key


class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(1920, 1080, "EasyTetris", fullscreen=True)
        
        self.game_state         = GAME_STATE_START
        
        self.title_label        = pyglet.text.Label('PYGLET TETRIS', font_name='Joystix Monospace', font_size=32, 
                                    x=self.width//2, y=2*self.height//3,
                                    color=BLACK_COLOR2,
                                    anchor_x='center', anchor_y='center')
        self.start_label        = pyglet.text.Label('Press SPACE to start', font_name='Joystix Monospace', font_size=24, 
                                    x=self.width//2, y=self.height//3,
                                    color=BLACK_COLOR2,
                                    anchor_x='center', anchor_y='center')
        self.gameover_label     = pyglet.text.Label('GAME OVER', font_name='Joystix Monospace', font_size=24, 
                                    x=self.width//2, y=self.height//3,
                                    color=BLACK_COLOR2,
                                    anchor_x='center', anchor_y='center')
        self.grid = None

        self.push_down_cmd      = False
        self.push_left_cmd      = False
        self.push_right_cmd     = False
                
        pyglet.clock.schedule_interval(self.update, 1)
        pyglet.clock.schedule_interval(self.handle_down_pushes, 1/20)
        pyglet.clock.schedule_interval(self.handle_horiz_pushes, 1/4)
        
        self.bg = pyglet.shapes.Rectangle(0, 0, 1920, 1080, color=(255, 255, 255))

    def on_draw(self):
        self.clear()
        self.bg.draw()
        if self.game_state == GAME_STATE_START:
            self.title_label.draw()
            self.start_label.draw()
        if self.game_state == GAME_STATE_GAMEOVER:
            self.gameover_label.draw()
        if self.game_state == GAME_STATE_PLAYING:
            self.grid.draw()

    def on_key_press(self, symbol, modifiers):
        # exit game on ESC key press
        if symbol == key.ESCAPE:
            self.close()
            
        if self.game_state == GAME_STATE_PLAYING:
            if symbol == key.LEFT:
                self.push_left_cmd = True
                self.grid.move_block_left()
            if symbol == key.RIGHT:
                self.push_right_cmd = True
                self.grid.move_block_right()
            if symbol == key.DOWN:
                self.push_down_cmd = True
                self.grid.move_block_down()
            if symbol == key.SPACE:
                self.grid.rotate_block()

        if self.game_state in (GAME_STATE_START, GAME_STATE_GAMEOVER):
            if symbol == key.SPACE:
                self.start_game()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.push_left_cmd = False
        if symbol == key.RIGHT:
            self.push_right_cmd = False
        if symbol == key.DOWN:
            self.push_down_cmd = False

    def update(self, dt):
        if self.game_state == GAME_STATE_PLAYING:
            self.grid.move_block_down()

    def handle_down_pushes(self, dt):
        if self.game_state == GAME_STATE_PLAYING:
            if self.push_down_cmd:
                self.grid.move_block_down()

    def handle_horiz_pushes(self, dt):
        if self.game_state == GAME_STATE_PLAYING:
            if self.push_left_cmd:
                self.grid.move_block_left()
            if self.push_right_cmd:
                self. grid.move_block_right()
    
    def game_over(self):
        self.game_state = GAME_STATE_GAMEOVER
    
    def start_game(self):
        self.game_state = GAME_STATE_PLAYING
        self.grid = Grid(self)

if __name__ == '__main__':
    window = GameWindow()
    pyglet.app.run()
