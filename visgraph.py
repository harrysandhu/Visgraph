import sys
import pyglet
from pyglet.window import key, mouse
from pyglet import shapes
import numpy as np
from app.node import Node
from app.line import Line

data = [3, 4, 1, 2, 5, 7, 9, 24, 25]
edges = [(0,1), (2, 1), (2,0), (4, 3), (2, 5), (0, 4), (0, 6)]


window = pyglet.window.Window(width=1200, height=800)
batch = pyglet.graphics.Batch()

NODES = []
LINES = []


def create_graph():
    for i in range(len(data)):
        rx = np.random.randint(200, window.width-200)
        ry = np.random.randint(100, window.height-100)
        node = Node(data[i], rx, ry, batch)
        NODES.append(node)

    for e in edges:
        line = Line(NODES[e[0]], NODES[e[1]])
        LINES.append(line)




@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    for node in NODES:
        if node.x in range(x-30, x+30) and node.y in range(y-30, y+30):
            node.move(x+dx, y+dy)
            for line in LINES:
                if line.sNode == node:
                    line.move_start(node)
                elif line.eNode == node:
                    line.move_end(node)
            break

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        pyglet.app.exit()


@window.event
def on_draw():
    window.clear()
    for edge in LINES:
        edge.line.draw()
    batch.draw()
    for n in NODES:
        n.label.draw()

    

def main():
    create_graph()
    pyglet.app.run()

if __name__=="__main__":
    main()
