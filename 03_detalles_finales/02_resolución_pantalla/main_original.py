import pyglet


WINDOW_WIDTH    = 1280
WINDOW_HEIGHT   = 720


window  = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Pyglet Experiments", resizable=False)

batch   = pyglet.graphics.Batch()

tile_image = pyglet.image.load('bricks_tile.png')


width_in_tiles  = 1280 // 128
height_in_tiles  = 720 // 128

print('width in tiles: ', str(width_in_tiles+1))
print('height in tiles: ', str(height_in_tiles+1))

sprites = []

for i in range(0, width_in_tiles+1):
    for j in range(0, height_in_tiles+1):
        sprites.append( pyglet.sprite.Sprite(tile_image, x = i*128, y = j*128, batch=batch) )


@window.event
def on_draw():
    window.clear()
    batch.draw()

if __name__ == "__main__":
    pyglet.app.run()
