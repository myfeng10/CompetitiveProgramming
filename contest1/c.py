class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        self.visited = []
        self.parent = []

    def BFS(self, s, t):
        self.visited = [False] * (self.ROW)
        self.parent = [-1] * (self.ROW)
        queue = []

        queue.append(s)
        self.visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if self.visited[ind] == False and val > 0:
                    queue.append(ind)
                    self.visited[ind] = True
                    self.parent[ind] = u
        return True if self.visited[t] else False

    def FordFulkerson(self, source, sink):
        max_flow = 0

        while self.BFS(source, sink):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[self.parent[s]][s])
                s = self.parent[s]
            max_flow += path_flow
            v = sink
            while(v != source):
                u = self.parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = self.parent[v]
        return max_flow

    def minCut(self,source,edges):
        self.BFS(source, len(self.graph) - 1)
        reachable = self.visited

        min_edges = []
        for edge in edges:
            i,j=edge
            if reachable[i] and not reachable[j]: # if the edge goes from a reachable node to an unreachable node -> it is a min cut edge
                min_edges.append(edge)
        return min_edges


n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
edges  = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a-1, b-1))
    edges.append((b-1, a-1))
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

g = Graph(graph)

source = 0
sink = n - 1

max_flow = g.FordFulkerson(source, sink)
min_cut_edges = g.minCut(source,edges)

print(len(min_cut_edges))
for edge in min_cut_edges:
    print(edge[0] + 1, edge[1] + 1)
