import networkx as nx

n = int(input())
class friend:
    def __init__(self,n):
       self.nodes = {i:set() for i in range(n)}

    def __str__(self):
        return "\n".join(f"Node {node}: {self.nodes[node]}" for node in self.nodes)

    def add_friend(self,n1,n2) -> bool:
        # check if n2 is included in n1's enemy list
        if Enemy.is_enemy(n1,n2):
            return False
        
        # transitivity
        # find n1's friend, add them to n2's friend list
        for node in Friend.nodes[n1]:
            Friend.nodes[n2].add(node)
            Friend.nodes[node].add(n2)
        # find n2's friend, add them to n1's friend list
        for node in Friend.nodes[n2]:
            Friend.nodes[n1].add(node)
            Friend.nodes[node].add(node)
        # if not, add their relationship
        self.nodes[n1].add(n2)
        self.nodes[n2].add(n1)

        res1 = self.enemy_of_friend(n1,n2)
        if not res1:
            #print("enemy")
            return False
        return True
    
    def is_friend(self,n1,n2) -> bool:
        if n2 in self.nodes[n1]:
            return True
        return False
        
    def enemy_of_friend(self,n1,n2) -> bool:
        # find n2's enemy, add them to n1's enemy list
        for node in Enemy.nodes[n2]:
            if self.is_friend(node,n2):
                #print("Friend, enemyoffriend",node,n2)
                return False
            Enemy.nodes[node].add(n1)
            Enemy.nodes[n1].add(node)
        
        for node in Enemy.nodes[n1]:
            if self.is_friend(node,n1):
                #print("friend,enemyof friend",node,n1)
                return False
            Enemy.nodes[node].add(n2)
            Enemy.nodes[n2].add(node)
        return True
    
class enemy:
    def __init__(self,n):
        self.nodes = {i:set() for i in range(n)}

    def __str__(self):
        return "\n".join(f"Node {node}: {self.nodes[node]}" for node in self.nodes)

    def add_enemy(self,n1,n2) -> bool:
        # check if they are already friend
        if Friend.is_friend(n1,n2):
            return False
        self.nodes[n1].add(n2)
        self.nodes[n2].add(n1)

        res1 = self.friend_for_common_enemy(n1,n2) # return false if find conflict
        res2 = self.enemy_of_friend(n1,n2) # return false if finds conflict
        if (not res1) or (not res2):
            # if any return false: 
            return False
        return True
       
    def is_enemy(self,n1,n2) -> bool:
        if n2 in self.nodes[n1]:
            return True
        return False
    
    def friend_for_common_enemy(self,n1,n2) -> bool:
        # A common enemy makes two people friends
        # find the enemy of n1, add friend between it and n2
        for node in Enemy.nodes[n1]:
            # check if they are already enemy: conflict
            if Enemy.is_enemy(node,n2):
                #print("1.enemy,friend,",node,n1,n2)
                return False
            if node not in Friend.nodes[n2]:
                Friend.nodes[node].add(n2)
                Friend.nodes[n2].add(node)
        # find the enemy of n2, add friend between it and n1
        for node in Enemy.nodes[n2]:
            # if conflict
            if Enemy.is_enemy(node,n1):
                #print("2.enemy,friend,",node,n1,n2)
                return False
            Friend.nodes[node].add(n1)
            Friend.nodes[n1].add(node)
        return True

    def enemy_of_friend(self,n1,n2) -> bool:
        # find enemy of a friend when enemy gets updated:
        # find friends with n1, add them to n2's enemy
        for node in Friend.nodes[n1]:
            if Friend.is_friend(node,n2):
                #print("1.enemy, enemyoffriend",node,n2,n1)
                return False
            self.nodes[n2].add(node)
            self.nodes[node].add(n2)

        # find friends with n2, add them to n1's enemy
        for node in Friend.nodes[n2]:
            if Friend.is_friend(node,n1):
                #print("2.enemy, enemyoffriend",node,n2,n1)
                return False
            self.nodes[n1].add(node)
            self.nodes[node].add(n1)
        return True
        

Friend = friend(n)
Enemy = enemy(n)
#print("Friend",Friend)
#print("Enemy",Enemy)
while True:
    opp,a,b = map(int, input().split())
    if opp==0 and a==0 and b==0:
        break
    
    if opp ==1:
        # set enemy
        res = Friend.add_friend(a,b)
        if not res:
            print(-1)
    elif opp==2:
        # set enemy
        res = Enemy.add_enemy(a,b)
        if not res:
            print(-1)
    elif opp ==3:
        # is friend?
        res = Friend.is_friend(a,b)
        if res:
            print(1)
        else:
            print(0)
    else:
        # is enemy?
        res = Enemy.is_enemy(a,b)
        if res:
            print(1)
        else:
            print(0)
    #print("Friend",Friend)
    #print("Enemy",Enemy)