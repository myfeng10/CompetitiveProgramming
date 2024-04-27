
n= list(map(int,input().split()))
mintrack = 0
if n[1]==1 or n[2]==1 or n[1]+n[2] ==n[0]:
    print(1)
else:
    for numa in range(1,n[0]):
        numb = n[0]-numa
        ashare = int(n[1]/numa)
        bshare = int(n[2]/numb)
        #print(ashare,bshare,numa,numb)
        mintrack = max(mintrack,min(ashare,bshare))
    print(mintrack)


