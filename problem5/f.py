l,a = map(int, input().split())
s = input()
left = list(map(str, input().split()))


dp=[0]*(l+1)
dp[0]=0
inc = [0]*(l+1)
inc[0]=0

for i in range(l):
    if s[i] in left:
        if i>0 and dp[i]==dp[i-1]:
            inc[i+1]=1
            dp[i+1]=dp[i]+inc[i+1]
        else:
            inc[i+1]=inc[i]+1
            dp[i+1] = dp[i]+inc[i+1]
    else:
        dp[i+1] = dp[i]
        inc[i+1]= 0

print(dp[-1])


