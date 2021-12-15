from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.number_of_vertexes = 0
        self.graph = defaultdict(list)
        self.visited = set()
        self.stack = []
        self.ids = {}
        self.low_links = {}
        self.counter = 0
        self.scc = []

    def read_data(self, name_in_file):
        with open(name_in_file, 'r') as tarjan_in_file:
            self.number_of_vertexes, number_of_edges = map(int, tarjan_in_file.readline().split(" "))
            for i in range(number_of_edges):
                list_data = list(map(int, tarjan_in_file.readline().split(" ")))
                self.graph[list_data[0]].append(list_data[1])
  
    def tarjan_util(self, vertex_start):
        if vertex_start not in self.visited:
            self.ids[vertex_start] = self.counter
            self.low_links[vertex_start] = self.counter
            self.counter += 1
            self.visited.add(vertex_start)
            self.stack.append(vertex_start)
            
            for vertex_next in self.graph[vertex_start]:
                if vertex_next not in self.visited:
                    self.tarjan_util(vertex_next)
                    self.low_links[vertex_start] = min(self.low_links[vertex_next], self.low_links[vertex_start])
                elif vertex_next in self.stack:
                    self.low_links[vertex_start] = min(self.low_links[vertex_next], self.low_links[vertex_start])
            
            if self.low_links[vertex_start] == self.ids[vertex_start]:
                current_scc = [vertex_start]
                vertex = self.stack.pop()
                while vertex != vertex_start:
                    current_scc.append(vertex)
                    vertex = self.stack.pop()
                self.scc.append(current_scc)
    
    def tarjan(self):
        for vertex in self.graph:
            self.tarjan_util(vertex)
        return self.scc