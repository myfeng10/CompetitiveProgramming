m = input()
while m != "#":
    m = list(m)
    d = list(input())
    print(m)
    print(d)
    
    dp = [0]*(len(m)+1)
    for i in range(1,len(m)+1):
        eleM = m[i-1]
        eleD = d[i-1]
        if eleM in d and d.index(eleM)<i:         # if the newest element from m has appeared in d
            dp[i] = dp[i-1]+1                                   # a valid country to visit
        
        elif eleD in m and m.index(eleD)<i:          # if the newest element from d has appeared in m
            dp[i] = dp[i-1]+1                                   # a valid country to visit

        else:
            dp[i] = dp[i-1]                                       # not a valid country to visit
    print(dp)
    m = input()