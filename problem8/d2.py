import sys
input=sys.stdin.readline
n = int(input())

for _ in range(n):
    phone = int(input())
    number = []
    dict={}
    
    for _ in range(phone):
        newPhone = str(input().strip())
        for i in range(1, len(newPhone)+1):
            substring = newPhone[:i].strip()
            if substring not in dict:
                dict[substring]=1
            else:
                dict[substring]+=1
        number.append(newPhone)

    isvalid = True

    for key in number:
        if dict[key] != 1:
            isvalid=False
            continue
    
    if isvalid:
        print("YES")
    else:
        print("NO")
    
    # print(dict)