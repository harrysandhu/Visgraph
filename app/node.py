import pyglet
from pyglet import shapes
import numpy as np

STATE = {
    "undiscovered" : (50, 50, 50),
    "discovered": (64, 118, 219),
    "processed": (255, 0, 0)
}
class Node:
    def __init__(self, value, x, y, batch):
        self.value = value
        self.circle = shapes.Circle(x, y, 30, batch=batch, color=STATE["discovered"])
        self.label = pyglet.text.Label(str(value), font_size=10, x=x, y=y, 
                                        anchor_x='center', anchor_y='center')             
        self.x = x
        self.state = STATE["undiscovered"]
        self.y = y 

    def move(self, x, y):
        self.x, self.y = x, y
        self.circle.x, self.circle.y = x, y
        self.label.x, self.label.y = x, y


    def changeState(self, state):
        if state in STATE:
            self.state = state
            self.circle.color = STATE[state]

        