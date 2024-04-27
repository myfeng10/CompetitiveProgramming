import heapq
def dijkstra(graph, start):
    # The graph is represented as a dictionary of dictionaries:
    #   - Outer dictionary: Node -> Inner dictionary
    #   - Inner dictionary: Adjacent Node -> Edge Weight
    
    # Create a dictionary to store the shortest path distance from start to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    # Priority queue to process nodes based on shortest path distance
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Nodes can only be added once to the queue
        if current_distance > shortest_paths[current_node]:
            continue
        
        # Process each adjacent node to the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

n, m = map(int, input().split())
graph = {i: {} for i in range(n)} 

for _ in range(m):
    a, b, w = map(int, input().split())
    a, b = a - 1, b - 1 
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], w) 
    else:
        graph[a][b] = w  # Add new edge

path = dijkstra(graph, 0)
for node, distance in path.items():
    print(distance, end=" ")