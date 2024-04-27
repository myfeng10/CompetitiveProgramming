n = int(input())
for i in range(n):
    a,b,c = list(map(int, input().split()))
    if a <= 20 and b <=20 and c<=20:
        print("Case",str(i+1)+":","good")
    else:
        print("Case",str(i+1)+":","bad")
