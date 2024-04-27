n = int(input())
for _ in range(n):
    string = input()
    iteration = (len(string)-1)//2
    found = False
    # print("string",string)
    for i in range(iteration):     
        firstpart = string[len(string)-2-i-i:len(string)-1-i]
        secondpart = string[len(string)-i-1:]
        # print(firstpart,secondpart)
        # print(string[len(string)-i-1:])                                             # second part
        # print(string[len(string)-i-i:len(string)-i])                              # first part
        if firstpart == secondpart:
            print("YES")
            found =True
            break
    if not found:
        print("NO")
