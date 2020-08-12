#!/usr/bin/env python3
import numpy as np
from .node import Node
from .line import Line


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
        self.q = []
        self.bfs_data = []
        self.dfs_data = [] 
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

    def adj(self, node_index):
        
        enodes = self.edges[self.NODES[node_index]]
        print(enodes)
        indices = [self.NODES.index(i) for i in enodes]
        return indices

    def bfs(self, start):
        nodes = [-1 for i in range(len(self.data))]

        q = []
        q.append(start)
        nodes[start] = 0
        self.bfs_data.append(nodes.copy())

        while len(q) > 0:
            v = q.pop(0)
            nodes[v] = 0
            self.bfs_data.append(nodes.copy())
            for w in self.adj(v):
                if nodes[w] == -1:
                    q.append(w)
            nodes[v] = 1
            self.bfs_data.append(nodes.copy())

    def dfs(self, start):
        nodes = [-1 for i in range(len(self.data))]
        s = []
        s.insert(0,start)
        self.dfs_data.append(nodes.copy())

        while len(s) > 0:
            v = s.pop(0)
            
            if nodes[v] == -1
                nodes[v] = 0
                self.dfs_data.append(nodes.copy())
                for w in self.adj(v):
                    s.insert(0, w)
                nodes[v] = 1
                self.dfs_data.append(nodes.copy())