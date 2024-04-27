n = int(input())
friend = {i:set() for i in range(n)}
enemy = {i:set() for i in range(n)}
while True:
    opp,a,b = map(int,input().split())
    if opp==0 and a == 0 and b==0:
        break
    if opp == 1:
        if a in enemy[b]:
            print(-1)
            continue

        # transitivity
        for node in friend[a]:
            if node in enemy[b]:
                print(-1)
                continue
            friend[node].add(b)
            friend[b].add(node)
        for node in friend[b]:
            if node in enemy[a]:
                print(-1)
                continue
            friend[node].add(a)
            friend[a].add(node) 
        friend[a].add(b)
        friend[b].add(a)

        # find b's enemy and set them to a's enemy
        for node in enemy[b]:
            if node in friend[a]:
                print(-1)
                continue
            enemy[a].add(node)
            enemy[node].add(a)
        for node in enemy[a]:
            if node in friend[b]:
                print(-1)
                continue
            enemy[b].add(node)
            enemy[node].add(b)
        #print("friend,", friend)
        #print("enemy,", enemy)
    elif opp == 2:
        if a in friend[b]:
            print(-1)
            continue
        enemy[a].add(b)
        enemy[b].add(a)

        ## common enemy -> friend: if a and b are enemies: 
        # find enemy of b and set them to a's friend
        for node in enemy[b]:
            if a in enemy[node]:
                print(-1)
                continue
            friend[node].add(a)
            friend[a].add(node)

        # find enemy of a and set them to b's friend
        for node in enemy[a]:
            if b in enemy[node]:
                print(-1)
                continue
            friend[node].add(b)
            friend[b].add(node)

        # enemy of friend is enemy: if a and b are enemy: 
        # find a's friend and set them to b's enemy
        for node in friend[a]:
            if node in friend[b]:
                print(-1)
                continue
            enemy[b].add(node)
            enemy[node].add(b)
        
        # find b's friend and set them to a's enemy
        for node in friend[b]:
            if node in friend[a]:
                print(-1)
                continue
            enemy[a].add(node)
            enemy[node].add(a)    
        #print("friend,", friend)
        #print("enemy,", enemy)

    elif opp == 3:
        # is friend
        if a in friend[b] or a==b:
            print(1)
        else:
            print(0)
    else:
        # is enemy
        if a in enemy[b]:
            print(1)
        else:
            print(0)
        