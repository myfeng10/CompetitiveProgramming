class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        self.visited = []
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        self.visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
    

    def minCut(self, source,edges):
        self.BFS(source, len(self.graph) - 1)
        reachable = self.visited

        min_edges = []
        for edge in edges:
                i,j=edge
                if reachable[i] and not reachable[j]: # if the edge goes from a reachable node to an unreachable node -> it is a min cut edge
                    min_edges.append((i, j))

        return min_edges
    


n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
edges  = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a-1, b-1))
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