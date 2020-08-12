#!/usr/bin/env python3

import sys
import pyglet
from pyglet.window import key, mouse
from pyglet import shapes
import numpy as np
from app.node import Node
from app.line import Line
from app.graph import Graph
from pyglet import clock

data = [3, 4, 1, 2, 5, 7, 9, 24, 25, 34, 26, 314, 343, 75, 78, 99, 10, 42, 11, 12, 432, 5352, 45]
edges = [(0,1),
         (2, 1), 
         (2,0),
         (4, 3), 
         (2, 5), 
         (0, 4), 
         (0, 6), 
         (4,5), 
         (6,9), 
         (2, 9), 
         (2, 11), 
         (1, 4),
         (8, 9),
         (10, 12),
         (10, 0)
        ]


window = pyglet.window.Window(width=1200, height=800)
batch = pyglet.graphics.Batch()


graph = Graph(directed=False, data=data, edges=edges, batch=batch, window=window)

for k in graph.edges:
    print(str(k.value) + "->", end="")
    for v in graph.edges[k]:
        print(str(v.value) + " - ", end="")

    print("")


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    for node in graph.NODES:
        if node.x in range(x-30, x+30) and node.y in range(y-30, y+30):
            node.move(x+dx, y+dy)
            for line in graph.LINES:
                if line.sNode == node:
                    line.move_start(node)
                elif line.eNode == node:
                    line.move_end(node)
            break


def cState(t, bd):
    for i in range(len(bd)):
        if bd[i] == -1:
            graph.NODES[i].changeState("undiscovered")
        elif bd[i] == 0:
            graph.NODES[i].changeState("discovered")
        else:
            graph.NODES[i].changeState("processed")


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        pyglet.app.exit()
    if symbol == key.SPACE:
        graph.bfs(0)
        bd = graph.bfs_data
        for i in range(0, len(bd)):
            clock.schedule_once(cState, i, bd[i])
    


@window.event
def on_draw():
    window.clear()
    for edge in graph.LINES:
        edge.line.draw()
    batch.draw()
    for n in graph.NODES:
        n.label.draw()

    

def main():
    pyglet.app.run()

if __name__=="__main__":
    main()
