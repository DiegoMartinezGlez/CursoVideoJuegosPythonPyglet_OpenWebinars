import pyglet


class Platform():
    def __init__(self, x, y, width, height, batch):
        self.width      = width
        self.height     = height
        self.rect       = pyglet.shapes.Rectangle(x, y, self.width, self.height, color=(80, 80, 80), batch=batch)

    def draw(self):
        self.batch.draw()
    
    def contains(self, x, y):
        if x<=self.rect.x or x>=self.rect.x+self.rect.width:
            return False
        if y<=self.rect.y or y>=self.rect.y+self.rect.height:
            return False

        return True
