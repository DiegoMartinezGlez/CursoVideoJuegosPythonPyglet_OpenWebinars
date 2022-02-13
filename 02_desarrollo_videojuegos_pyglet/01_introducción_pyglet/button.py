import pyglet


class Button:
    def __init__(self, x, y, width, height, text):

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.batch  = pyglet.graphics.Batch()

        self.label  = pyglet.text.Label(text,
                            font_name='Retro Computer',
                            font_size=36,
                            x=self.x, y=self.y,
                            anchor_x='center', anchor_y='center')

        self.rect   = pyglet.shapes.Rectangle(self.x - self.width//2, y - self.height//2, self.width, self.height, 
                                            color=(185, 155, 55), 
                                            batch=self.batch)

    def draw(self):
        self.batch.draw()
        self.label.draw()

