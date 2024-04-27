def edge_to_vertex_dual(G):
    D = {}
    for x in G:
        for y in G[x]:
            if (y, x) not in D:
                D[(x,y)] = set()
    for x in G:
        for y in G[x]:
            for z in G[x]:
                if y != z:
                    D[tuple(sorted([x, y]))].add(tuple(sorted([x, z])))
                    #D[tuple(sorted([x, z]))].add(tuple(sorted([x, y])))
    return D


G = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

sampleGraph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'C', 'D'], 
    'C' : ['A','B','D'],
    'D' : ['B','C']
}

for x in G:
    print(x, G.get(x))
print()
D = edge_to_vertex_dual(G)
for x in D:
    print(x, D.get(x))

print()

for x in sampleGraph:
    print(x, sampleGraph.get(x))
print()
D1 = edge_to_vertex_dual(sampleGraph)
for x in D1:
    print(x, D1.get(x))
