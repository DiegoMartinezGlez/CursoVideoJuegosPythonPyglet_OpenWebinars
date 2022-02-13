import pyglet

WINDOW_WIDTH    = 1280
WINDOW_HEIGHT   = 720

pyglet.font.add_file('fonts/joystix.ttf')
joystix = pyglet.font.load('fonts/joystix.ttf', 16)
FONT_TYPE = "Joystix Monospace"


ACTION_PLAY     = "action_play"