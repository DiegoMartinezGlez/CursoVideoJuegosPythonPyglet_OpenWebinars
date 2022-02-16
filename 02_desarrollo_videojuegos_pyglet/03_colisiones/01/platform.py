import pyglet


class Platform():
    def __init__(self, x, y, width, height):
        self.width      = width
        self.height     = height
        self.rect       = pyglet.shapes.Rectangle(x, y, self.width, self.height, color=(80, 80, 80))

    def draw(self):
        self.rect.draw()
