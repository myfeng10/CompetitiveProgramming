MOD = 10**9 + 7
N = 10**5 + 5

dp = [0] * (N * 2)

for i in range(10):
    dp[i] = 1
for i in range(10, N * 2):
    dp[i] = (dp[i - 9] + dp[i - 10]) 
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    while n:
        ans += dp[n % 10 + k]
        ans %= MOD
        n //= 10
    print(ans)

