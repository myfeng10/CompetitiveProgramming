test = int(input())
for _ in range(test):
    n,m,k = map(int,input().split())
    if (n*m)-1 == k:
        print("YES")
    else:
        print("NO")