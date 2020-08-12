#!/usr/bin/env python3
import numpy as np
from .node import Node
from .line import Line
import time

from pyglet import clock


class Graph:
    def __init__(self, directed, data, edges, batch, window):
        self.directed = directed
        self.batch = batch
        self.window = window
        self.nvertices = len(data)
        self.nedges = len(edges)
        self.LINES = []
        self.NODES = []
        self.edges = {}
        self.data = data
        self.i = 0

        for i in range(len(data)):
            rx = np.random.randint(200, window.width-200)
            ry = np.random.randint(100, window.height-100)
            node = Node(data[i], rx, ry, batch)
            self.NODES.append(node)
            self.edges.update({node: []})


        for e in edges:
            line = Line(self.NODES[e[0]], self.NODES[e[1]])
            self.LINES.append(line)
            if directed:
                self.edges[self.NODES[e[0]]].append(self.NODES[e[1]])
            else:
                self.edges[self.NODES[e[0]]].append(self.NODES[e[1]])
                self.edges[self.NODES[e[1]]].append(self.NODES[e[0]])


    def bfs(self, index):
        