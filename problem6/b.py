bc= int(input())
b = list(map(int, input().split()))
gc = int(input())
g = list(map(int, input().split()))

b.sort()
g.sort()

B=0
G=0
result=0
while (B<bc and G<gc):
    if abs(b[B]-g[G])<=1:
        B+=1
        G+=1
        result+=1
    elif b[B]>g[G]:
        G+=1
    else: # if g[G]>b[B] ->  need to increase b 
        B+=1

print(result)