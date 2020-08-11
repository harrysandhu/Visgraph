import pyglet
from pyglet import shapes
import numpy as np

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
