isFirst = True
while True:
    a = list(map(int, input().split()))
    if len(a) == 1:
        break
    if not isFirst:
        print()
    k = a[0]
    numbers = a[1:] 
    for a in range(0,k-5):
        for b in range(a+1,k-4):
            for c in range(b+1,k-3):
                for d in range(c+1,k-2):
                    for e in range(d+1,k-1):
                        for f in range(e+1, k):
                            print(numbers[a],numbers[b],numbers[c],numbers[d],numbers[e],numbers[f])
                            isFirst = False