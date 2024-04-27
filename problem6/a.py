from collections import deque
def bfs(node):
    queue = deque([(node,0)])
    track = 1
    while queue:
        node,i = queue.popleft()
        track=i
        for neighbour in graph[node]:
            queue.append([neighbour,i+1])
    return track+1

num = int(input())
l=[]
graph = {}
result = 0

for i in range(1,num+1): # initialize the graph
    l.append(int(input()))
    graph[i]=[]

for i in range(1,num+1): # form the graph
    node = l[i-1] 
    if node != -1:
        graph[node].append(i) 

for i in range(1,num+1): # search dfs
    if l[i-1] == -1:
        locallength = bfs(i)
        if locallength > result:
            result = locallength

print(result)


    




