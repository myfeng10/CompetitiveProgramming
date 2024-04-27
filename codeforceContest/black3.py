n = int(input())
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def __str__(self):
        result = ""
        for u in self.graph:
            result += f"{u}: "
            result += ", ".join(f"{v} ({weight})" for v, weight in self.graph[u])
            result += "\n"
        return result

    def edge_weight(self, u, v):
        if u in self.graph:
            for neighbor, weight in self.graph[u]:
                if neighbor == v:
                    return weight
        return -1
graph = Graph(n)
while True:
    opp,a,b = map(int,input().split())
    weight = graph.edge_weight(a,b)
    if opp == 1:
        weight = graph.edge_weight(a,b)
        if weight == 
