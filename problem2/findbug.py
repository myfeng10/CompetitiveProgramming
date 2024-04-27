def find_neighbour(index, N):
    ret = []
    for i in range(N):
        #Using XOR to flip i-th bit
        neighbor = index ^ (1 << i)
        ret.append(bin(neighbor))
    #print(bin(index), "ret",ret)
    return ret

while True:
    try:
        N = int(input())
    except EOFError:
        break

    # 1 << N is equivalent to 2^N: finding the number of corners
    n = 1 << N
    #print("n",n)
    a = []
    for _ in range(n):
        a.append(int(input()))
    #print("a",a)
    potency = [0 for _ in range(n)]
    for i in range(n):
        for j in find_neighbour(i, N):
            #If node i and j are neighbours we add the potency of node i by the weight of node j
            potency[i] += a[int(j, 2)]
    #print("potency",potency)
    ans = 0
    for i in range(n):
        for j in find_neighbour(i, N):
            #If node i and j are neighbours we find the sum of their potencies
            ans = max(ans, potency[i] + potency[int(j, 2)])
    
    print(ans)

    


    