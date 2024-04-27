
n,m = map(int,input().split())
parent = [i for i in range(n)]
size = [1]*n
def find(x):
    # finds the representative of node x

    # if we didnt reached the representative -> keep finding 
    if parent[x] != x:
        return find(parent[x])
    else:
        return x
    
def union(x,y):
    # given node x and y, first find find their representative, set one of them to be the representative of the other
    yRep = find(y)
    xRep = find(x)
    if xRep != yRep:
        # if not same component already
        parent[yRep] = xRep
        size[xRep] += size[yRep]
        # if size[yRep] > size[xRep]:
        #     # set xRep's parent to be yRep
        #     parent[xRep] = yRep
        #     size[yRep] += size[xRep]
        # else:
        #     parent[yRep] = xRep
        #     size[xRep] += size[yRep]
   
    # count the number of distinct number in parent + largest occurange
    count = {}
    for i in range(n):
        if parent[i] in count:
            count[parent[i]] +=1
        else:
            count[parent[i]] =1
    #print("count", count)
    print(len(count),max(count.values()))

component = n 
largestSize = 1 

for _ in range(m):
    x,y = map(int,input().split())
    if find(x-1) != find(y-1):
        component -= 1
        union(x-1,y-1)
        largestSize = max(largestSize,size[find(x-1)]) # x could always belongs to representative of y

