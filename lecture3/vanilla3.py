
t = int(input())
for _ in range(t):
    num = int(input())
    n = list(map(int,input().split()))
    i=2
    while True:
        mod = set()
        for ele in n:
            ans = ele%i
            set.add(ans)
        if len(mod) == 2:
            print(i)
            break
        i*=2
    
    
        