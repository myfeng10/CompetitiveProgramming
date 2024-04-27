n = int(input())
alist = []
for _ in range(n):
    x = int(input())
    alist.append(x)

def D(arr):
    def subroutine(a,b,c):
        dp = [0] * 3
        for i in range(len(arr)):
            dp[c] = max(dp[a], dp[b], dp[c])
            dp[b] = max(dp[a], dp[b])
            dp[arr[i]] += 1
        return max(dp)
    x1 = (subroutine(0,1,2))
    x2 = (subroutine(0,2,1))
    x3 = (subroutine(2,1,0))
    x4 = (subroutine(2,0,1))
    x5 = (subroutine(1,0,2))
    x6 = (subroutine(1,2,0))
    print(max(x1,x2,x3,x4,x5,x6) )

D(alist)