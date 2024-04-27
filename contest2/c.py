from collections import deque

def bfs(start, visited, graph):
    """ Perform BFS from the start node, marking all reachable nodes as visited """
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)

def count_connected_components(graph):
    n = len(graph)  
    visited = [False] * n
    component_count = 0
    
    for i in range(n):
        if not visited[i]: 
            bfs(i, visited, graph)
            component_count += 1  
    
    return component_count

n, k, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for _ in range(m):
    input()  

print(count_connected_components(graph) - 1)
