from collections import deque

NIL = 0 
INF = 1 << 32 # set to infinity 

#Is Correct
def bfs(k):
    Q = deque()
    # print("BFS: Pair_U: ", Pair_U)
    for i in range(1, n+1):
        if Pair_U[i] == NIL:
            Dist[i] = 0
            Q.append(i)
        else:
            Dist[i] = INF
    # print("BFS: Pair_V: ", Pair_V)
    # print("BFS: Dist: ", Dist)
    Dist[NIL] = INF

    while(len(Q)):
        u = Q.popleft()

        if(Dist[u] < Dist[NIL]):
            for v, p in adj[u]: # v: factory, p: index of edge
                if(p <= k and Dist[Pair_V[v]] == INF):
                    Dist[Pair_V[v]] = Dist[u] + 1
                    Q.append(Pair_V[v])
    # print()
    # print("BFS: Pair_U: ", Pair_U)
    # print("BFS: Pair_V: ", Pair_V)
    # print("BFS: Dist: ", Dist)
    # print("--")
    return Dist[NIL] != INF


#Is Correct
def dfs(u, k):
    if u != NIL:
        for v, p in adj[u]:
            if(p <= k and Dist[Pair_V[v]] == Dist[u] + 1):
                if(dfs(Pair_V[v], k)):
                    Pair_V[v] = u
                    Pair_U[u] = v
                    return True
        Dist[u] = INF
        return False
    return True

#Is Correct
#Modified Hopcroft - Karp (See Ed Discussion for more info)
def HK(k):
    # print("k: "+str(k))
    cnt = 0

    global Pair_U
    Pair_U = [NIL for _ in range(n+1)]
    global Pair_V
    Pair_V = [NIL for _ in range(n+1)]
    global Dist
    Dist = [NIL for _ in range(n+1)]

    while(bfs(k)):
        for i in range(1, n+1):
            if(Pair_U[i] == NIL and dfs(i, k)):
                cnt += 1

    return cnt == n


n, m = [int(x) for x in input().split()]

adj = [[] for _ in range(n+1)]
edge = [[] for _ in range(m)]

for i in range(m):
    u, v, d = [int(x) for x in input().split()]
    edge[i] = [d, u, v]
edge.sort() # sorted by the days needed to build the road
for i in range(m):
    u, v = edge[i][1], edge[i][2] # u: airport, v: factory
    adj[u].append((v, i)) # adj[airport] = (factory, index of edge)

l=0
r = m
while l<r: # binary search to find minimum value of days needed, k is the index of such value
    k = (l+r)//2
    # print("k: "+str(k))
    # print("HK(k): ", HK(k))
    if HK(k): # if it is possible to find such value, 
        r=k
    else:
        l=k+1 # 

if l < m: 
    # print(edge)
    print(edge[l][0])
else:
    print(-1)

