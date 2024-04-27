n = int(input())
result = []
for i in range(1,n+1):
    inputint = list(map(int,input().split()))
    for j in range(n):
        if inputint[j] != -1:
            s = str(i) + " " + str(j+1) + " " + str(inputint[j])
            result.append(s)

print(len(result))
for i in range(len(result)):
    print(result[i])
