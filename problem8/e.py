n = int(input())
for _ in range(n):
    lens = int(input())
    s = input()
    sorted_chars = sorted(s) 
    count = 0
    for i in range(lens):
        if s[i] != sorted_chars[i]:
            count+=1
    print(count)

