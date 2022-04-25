import pyglet

GAME_STATE_START="state_start"
GAME_STATE_PLAYING="state_playing"
GAME_STATE_GAMEOVER="state_gameover"

BRICK_WIDTH=40

BLOCK_TYPE_O="o_type"
BLOCK_TYPE_I="i_type"
BLOCK_TYPE_T="t_type"
BLOCK_TYPE_L="l_type"
BLOCK_TYPE_J="J_type"
BLOCK_TYPE_S="s_type"
BLOCK_TYPE_Z="z_type"

BLOCK_TYPES=[BLOCK_TYPE_O, BLOCK_TYPE_I, BLOCK_TYPE_T, BLOCK_TYPE_L, BLOCK_TYPE_J, BLOCK_TYPE_S, BLOCK_TYPE_Z]

PANELS_WIDTH = BRICK_WIDTH*18


BG_COLOR            = (220, 220, 220)
BG_COLOR_DARK       = (180, 180, 180)
WHITE_COLOR         = (255, 255, 255)
BLACK_COLOR         = (0, 0, 0)
BLACK_COLOR2        = (0, 0, 0, 255)

pyglet.font.add_file('joystix.ttf')
retroFont = pyglet.font.load('joystix.ttf', 16)