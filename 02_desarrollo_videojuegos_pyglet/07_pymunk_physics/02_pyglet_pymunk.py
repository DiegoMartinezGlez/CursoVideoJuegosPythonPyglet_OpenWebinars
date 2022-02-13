import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import time


window = pyglet.window.Window(1280, 720, "Pyglet Pymunk Experiments", resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -500

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)




mass = 10
radius = 20
h = 200
circle_moment           = pymunk.moment_for_circle(mass, 0, radius)
circle_body             = pymunk.Body(mass, circle_moment)
circle_body.position    = 100, h
circle_shape            = pymunk.Circle(circle_body, radius)
circle_shape.elasticity = 0.9
circle_shape.friction   = 0.9
space.add(circle_body, circle_shape)

mass = 10
circle_moment2           = pymunk.moment_for_circle(mass, 0, radius)
circle_body2             = pymunk.Body(mass, circle_moment2)
circle_body2.position    = 1180, h
circle_shape2            = pymunk.Circle(circle_body2, radius)
circle_shape2.elasticity = 0.9
circle_shape2.friction   = 0.9
space.add(circle_body2, circle_shape2)


segment_shape                = pymunk.Segment(space.static_body, (0,40), (600,0), 5)
segment_shape.body.position  = 0, 100
segment_shape.elasticity     = 0.9
segment_shape.friction       = 0.9
space.add(segment_shape)

segment_shape2               = pymunk.Segment(space.static_body, (0,0), (600,40), 5)
segment_shape2.body.position = 680, 100
segment_shape2.elasticity    = 0.9
segment_shape2.friction      = 0.9
space.add(segment_shape2)



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/50)
    pyglet.app.run()