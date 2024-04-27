n = int(input())
for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    sum=0
    a.sort()
    start_index = m-1
    end_index = m
    while start_index >=0 and end_index <2*m:
        sum += abs(a[end_index] - a[start_index])
        start_index -=1
        end_index +=1
    
    print(sum)