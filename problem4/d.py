n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(int,input().split()))
    ldiff = [y - x for x, y in zip(l, l[1:])]
    if len(ldiff)==1:
        print("Case "+str(i+1)+": "+str(ldiff[0]))
        break
        
    k = max(ldiff)
    if ldiff.count(k)<=1:
        print(f"Case {i+1}: {k}")
    else:
        print(f"Case {i+1}: {k+1}")
