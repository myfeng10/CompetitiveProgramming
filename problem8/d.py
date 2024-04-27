n = int(input())
for _ in range(n):
    phone = int(input())
    number = []
    isvalid = True
    
    for _ in range(phone):
        newPhone = input()
        for i in range(len(number)):
            prev = number[i]
            if prev == newPhone[:len(prev)]:
                print("NO")
                isvalid=False
                continue
        if not isvalid:
            continue
        number.append(newPhone)
    if isvalid:
        print("YES")
    