# n,m=15,6
# cat = [[2,10],[3,5],[2,4],[7,7],[8,12],[11,11]]
# # n,m=5,10
# # cat = [[1,2],[3,4],[3,4],[3,4],[3,4],[1,1],[1,2],[3,3],[3,4],[3,4]]
# m,m=1000,1
# cat = [[1,1000]]
test = int(input())
for _ in range(test):
    n,m = map(int,input().split())
    cat = []
    for _ in range(m):
        cat.append(list(map(int, input().split())))
    dp = [0]*(n+1)
    dp[0] = 0
    cat.sort()

    for i in range(1,n+1):
        count = 0 # number of cat exposed in step i
        earliest = float("inf") # earliest cat exposed in step i
        for j in range(m):
            if cat[j][0]<=i and cat[j][1]>=i:
                count +=1
                earliest = min(earliest,cat[j][0])
        # print(i,":",count,earliest)       
                
        if count != 0 and earliest-1>0: # if found some cat
            # find the max cat before the earliest cat
            maxdp = max(dp[:earliest-1])
            # print(i,"max",maxdp,dp[:earliest-1])
            dp[i] = maxdp+count
        else:
            dp[i] = count


    #print(cat)
    # print(dp)
    print(max(dp))