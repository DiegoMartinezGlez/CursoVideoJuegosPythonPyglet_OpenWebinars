import pyglet


class Platform():
    def __init__(self, x, y, width, height, color, batch):
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.color      = color        
        self.rect       = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=self.color, batch=batch)

    def contains(self, x, y):
        if x < self.x or x > self.x+self.width:
            return False
        if y > self.y+self.height or y < self.y:
            return False

        return True