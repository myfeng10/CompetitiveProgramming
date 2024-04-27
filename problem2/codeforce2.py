t = int(input())

for _ in range(t):
    # for each test case
    _ = input() # empty line
    n,k = map(int,input().split()) # n: stations, k: queries
    #print("n",n,"k",k)
    s = list(map(int,input().split())) # s: stations information
    #print("station",s)
    # isPath = {}
    # for i in range(n):
    #     if s[i] not in isPath:
    #         isPath[s[i]] = []
    #     for j in range(i+1,n):
    #         if s[j] not in isPath[s[i]]:
    #             isPath[s[i]].append(s[j])
    indexBegin = {}
    indexEnd = {}
    for i in range(len(s)):
        # add the first occurance of s[i]
        if s[i] not in indexBegin:
            indexBegin[s[i]] = i
        # update the last occurance of s[i]
        if s[i] not in indexEnd:
            indexEnd[s[i]] = i
        else:
            if i > indexEnd[s[i]]:
                indexEnd[s[i]] = i
        
    for _ in range(k):
        # for each query
        a,b = map(int,input().split()) # a: start, b: end
        if a in indexBegin and b in indexEnd and indexBegin[a] < indexEnd[b]:
            print("YES")
        else:
            print("NO")
        #print("a",a,"b",b)
