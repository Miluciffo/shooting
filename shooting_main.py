import pyglet
import shoot
import shoting_сfg
from pyglet import shapes

window = pyglet.window.Window(800, 800)

back_batch = pyglet.graphics.Batch()
main_batch = pyglet.graphics.Batch()

circle = shapes.Circle(x=400, y=400, radius=50, color=color_shooting, batch=main_batch)
circle.opacity = 100

shoot_shape_list = []

for i in range(3):
    shoot_shape_list.append(
        shapes.Circle(x=-10, y=-10, radius=4, color=(255, 50, 255), batch=main_batch))
    shoot_shape_list[i].opacity = 100


@window.event
def on_draw():
    window.clear()
    back_batch.draw()
    main_batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        pass


@window.event
def on_mouse_motion(x, y, dx, dy):
    pass


pyglet.app.run()
