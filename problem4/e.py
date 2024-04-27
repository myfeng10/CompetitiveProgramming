

n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
#print(a)
minCount = 0
minSum = 0
for i in range(n+1):
    minSum += a[i]
    minCount += 1
    #print(minSum,sum(a)-minSum)
    if minSum > sum(a)-minSum:
        break
print(minCount)

