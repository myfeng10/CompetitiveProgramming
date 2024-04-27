
count=1
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    print("Case",str(count)+":",n-a.count(0)-a.count(0))
    count+=1

        
    


    