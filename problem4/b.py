input()
x = list(map(int,input().split()))

c = [0]*100001

# counting the number of each integers
for i in x:
    c[i]+=1

dp = {}

dp[1] = c[1]*1
dp[2] = c[2]*2
dp[3] = c[3]*3 + c[1]

score = 0

for i in range(4,100001):
    dp[i] = c[i]*i + max(dp[i-2],dp[i-3])
    score = max(score,dp[i])
    
print(score)