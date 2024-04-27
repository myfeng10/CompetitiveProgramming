
n = int(input())
for j in range(n):
    m = int(input()) 
    l = [0] + list(map(int, input().split()))  
    k = 0 
    final = 0 

    for i in range(1, n + 1):
        k = max(k, l[i] - l[i - 1])
    
    final = k  

    for i in range(1, n + 1):
        if l[i] - l[i - 1] == k:
            k -= 1
        elif l[i] - l[i - 1] > k:
            final += 1
            break

    print(f"Case {j+1}: {final}")
