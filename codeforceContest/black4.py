class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
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
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

n = int(input())

friend = UF(n)
enemy = {i:[] for i in range(n)}

while True:
    opp,a,b = map(int,input().split())
    if a==0 and b==0 and opp==0:
        break
    apar = friend.find(a)
    bpar = friend.find(b)
    if opp == 1:
        flag = True
        # if a and b are enemy (because a's friend is an enemy with b or vice versa): ie 
        for enemyID in enemy[a]:
            if bpar == friend.find(enemyID):
                print(-1) 
                flag=False
                continue
        for enemyID in enemy[b]:
            if apar == friend.find(enemyID):
                print(-1)
                flag=False
                continue
        if flag==True:
            friend.union(a,b)
            #print(friend.parent)
    elif opp == 2:
        enemy[apar].append(bpar)
        enemy[bpar].append(apar)
        #print(enemy)
    elif opp == 3:
        # just friend
        if apar == bpar:
            print(1)
            continue
        # a and b shared common enemy
        for ele in enemy:
            if apar in enemy[ele] and bpar in enemy[ele]:
                print(1)
                continue
        print(0)
    else:
        # a itself/friend is enemy with b or vice versa
        if apar in enemy[bpar] and bpar in enemy[apar]:
            print(1)
        else:
            print(0)