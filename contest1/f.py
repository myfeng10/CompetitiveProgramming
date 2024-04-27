n, k, d = map(int, input().split())

MOD = 1000000007

dp1 = [0] * (n+1)
dp2 = [0] * (n+1)
dp1[0]=1

for i in range(1, n+1): 
    for j in range(1, k+1):
        if i-j >=0:
            dp1[i] = (dp1[i] + dp1[i-j]) % MOD # dp1[i]: number of ways to reach i with out considering the d constraint

            if j>=d:
                dp2[i] = (dp2[i] + dp1[i-j]) % MOD
            else:
                dp2[i] = (dp2[i] + dp2[i-j]) % MOD
# print(dp1)
# print(dp2)
print(dp2[n])


