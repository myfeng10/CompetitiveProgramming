class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.size = [1 for i in range(n)] 
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX] 
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]  
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]  
n = int(input())
for _ in range(n):
    k = int(input())
    p = list(map(int, input().split()))

    ds = UF(k)
    for i in range(k):
        ds.union(i, p[i] - 1)

    for i in range(k):
        root = ds.find(i)
        print(ds.size[root], end=" ")
    print() 
