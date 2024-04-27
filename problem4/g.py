t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())

    l, r = [0 for _ in range(n)], [0 for _ in range(n)]
    
    for i in range(n):
        l[i], r[i] = [int(x) for x in input().split()]
    

    p, q = 0, 1000000000
    #Use Binary Search
    while p <= q:
    
        #m is the current step size
        m = (p + q) // 2
        #L is the leftmost position we can be and R is the rightmost position we can be. 
        L, R = 0, 0
        #ans is true iff m is a valid step size
        ans = True

        for i in range(n):
            #Keeping track of our L and R
            x, y = 0, 0
            if R + m < l[i]:
            
                ans = False
                break
            else:
                x = max(l[i], L - m)

            if L - m > r[i]:
                ans = False
                break
            else:
                y = min(r[i], R + m)

            L = x
            R = y
        
        if ans:
            q = m-1
        else:
            p = m+1

    print(p)

    