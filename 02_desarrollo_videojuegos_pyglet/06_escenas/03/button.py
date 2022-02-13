import pyglet
from pyglet import shapes
import config

BTN_STATE_DISABLED = "disabled"
BTN_STATE_OK = "ok"
COLOR_BROWN2 = (155, 105, 50, 255)
COLOR_BROWN_BG2 = (105, 54, 0, 255)
COLOR_YELL_FORE = (255, 204, 0)
COLOR_BROWNDARK = (155, 105, 0)
COLOR_YELL_DARK = (205, 154, 0)
COLOR_GREY_DARK =  (55, 55, 55)

class Button:
    def __init__(self, x, y, text, action):
        self.x = x
        self.y = y
        self.text = text
        self.action = action
        self.state  = BTN_STATE_OK
        self.label = pyglet.text.Label(self.text,
                        font_name = config.FONT_TYPE,
                        font_size = 24,
                        x = self.x, y = self.y,
                        anchor_x ='center', anchor_y ='center',
                        color = COLOR_BROWN_BG2)
        self.labelShadow = pyglet.text.Label(self.text,
                        font_name = config.FONT_TYPE,
                        font_size = 24,
                        x = self.x+2, y = self.y-2,
                        anchor_x ='center', anchor_y ='center',
                        color = COLOR_BROWN2)
        rectW = 400
        #rectW = self.label.content_width * 4.0
        rectH = self.label.content_height * 1.5
        rectX = self.x - rectW//2
        rectY = self.y - rectH//2
        self.rect = shapes.Rectangle(rectX, rectY, rectW, rectH, color=COLOR_YELL_FORE)
        self.rectShadow = shapes.Rectangle(rectX+2, rectY-2, rectW, rectH, color=COLOR_BROWNDARK)

    def draw(self):
        self.rectShadow.draw()
        self.rect.draw()
        self.labelShadow.draw()
        self.label.draw()

    def pointOn(self, x, y):
        x1 = self.rect.x
        y1 = self.rect.y
        x2 = x1 + self.rect.width
        y2 = y1 + self.rect.height
        return x1<x<x2 and y1<y<y2

    def mousePress(self, x, y):
        if self.state != BTN_STATE_DISABLED:
            on = self.pointOn(x,y)
            if on:
                return self.action
        return None

    def mouseOver(self, x, y):
        if self.state != BTN_STATE_DISABLED:
            on = self.pointOn(x,y)
            if on:
                self.rect.color  = COLOR_YELL_DARK
            else:
                self.rect.color  = COLOR_YELL_FORE

    def disable(self):
        self.state = BTN_STATE_DISABLED
        self.rect.color  = COLOR_GREY_DARK

    def enable(self):
        self.state = BTN_STATE_OK
        self.rect.color  = COLOR_YELL_FORE

    def btnFunc(self):
        pass
