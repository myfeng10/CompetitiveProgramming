from collections import deque

NIL = 0 
INF = 1 << 32

#Is Correct
def bfs():
    Q = deque()

    for i in range(1, n+1):
        if Pair_U[i] == NIL:
            Dist[i] = 0
            Q.append(i)
        else:
            Dist[i] = INF
            
    Dist[NIL] = INF

    while(len(Q)):
        u = Q.popleft()

        if(Dist[u] < Dist[NIL]):
            for v in adj[u]:
                if(Dist[Pair_V[v]] == INF):
                    Dist[Pair_V[v]] = Dist[u] + 1
                    Q.append(Pair_V[v])

    return Dist[NIL] != INF

#Is Correct
def dfs(u):
    if u != NIL:
        for v in adj[u]:
            if(Dist[Pair_V[v]] == Dist[u] + 1):
                if(dfs(Pair_V[v])):
                    Pair_V[v] = u
                    Pair_U[u] = v
                    return True
        Dist[u] = INF
        return False
    return True

#Is Correct
#Modified Hopcroft - Karp (See Ed Discussion for more info)
def HK():
    cnt = 0

    global Pair_U
    Pair_U = [NIL for _ in range(n+1)]
    global Pair_V
    Pair_V = [NIL for _ in range(m+1)]
    global Dist
    Dist = [NIL for _ in range(n+1)]

    while(bfs()):
        for i in range(1,n+1):
            if(Pair_U[i] == NIL and dfs(i)):
                cnt += 1

    return cnt

n, m, k = map(int, input().split()) #n boys, m girls, k potential pairs


adj = [[] for _ in range(n+1)]

for i in range(k):
    a,b = [int(x) for x in input().split()]
    adj[a].append(b) 

count = HK()



print(count)

for i in range(1, n+1):
    if Pair_U[i] != NIL:
        print(f"{i} {Pair_U[i]}")

# 2
# 1 2
# 2 1

# 3 2 4
# 1 1
# 1 2
# 2 1
# 3 1