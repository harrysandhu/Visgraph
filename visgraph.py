import sys
import pyglet
from pyglet.window import key, mouse
from pyglet import shapes
import numpy as np





data = [3, 4, 1, 2, 5, 7, 9, 24, 25]
edges = [(0,1), (2, 1), (2,0), (4, 3), (2, 5), (0, 4), (0, 6)]





window = pyglet.window.Window(width=1200, height=800)
batch = pyglet.graphics.Batch()


class Node:
    def __init__(self, value, x, y, batch):
        self.value = value
        self.circle = shapes.Circle(x, y, 30, batch=batch, color=(50, 50, 50))
        self.label = pyglet.text.Label(str(value), font_size=10, x=x, y=y, 
                                        anchor_x='center', anchor_y='center')             
        self.x = x
        self.y = y 

    def move(self, x, y):
        self.x, self.y = x, y
        self.circle.x, self.circle.y = x, y
        self.label.x, self.label.y = x, y

class Line:
    def __init__(self, sNode, eNode):
        self.sNode = sNode
        self.eNode = eNode
        self.line = shapes.Line(sNode.x, sNode.y,
                                eNode.x, eNode.y, width=4, color=(255, 255, 255))

    def move_start(self, node):
        self.sNode = node
        self.line.x, self.line.y = node.x, node.y
    
    def move_end(self, node):
        self.eNode = node
        self.line.x2, self.line.y2 = node.x, node.y




class Graph:
    def _init__(self, directed):
        self.directed = directed
        self.edges = 2


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
