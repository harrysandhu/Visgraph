import pyglet
from pyglet import shapes
import numpy as np

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



