t = int(input())
while t > 0:
    t -= 1
    s = input()

    #S is s but without dash
    S = ""
    dashcount = 0
    for i in range(len(s)):
        if s[i] != '-':
            S += s[i]
        else:
            dashcount += 1

   
        
    #Invalid if s has 2 consecutive dashes
    x = False
    if len(S)!=10:
        print("invalid")
        continue

    # 2 consequtive -
    for i in range(len(s)-1):
        if s[i]==s[i+1] and s[i+1]=='-':
            print("invalid")
            x = True
            break
    
    if x: 
        continue

    #Invalid if X is not in the last character
    for i in range(len(s)-1):
        if s[i] == 'X':
            print("invalid")
            x = True
            break

    if x: 
        continue

    #Invalid if first/last character is a dash
    if s[0]=='-' or s[-1]=='-':
        print("invalid")
        continue


    #Invalid if s has 3 dashes and the last dash is not at the second to last character
    if dashcount ==3  and s[11] != '-':
        print("invalid")
        continue


    #Code for checksum digit: Assume correct
    sum = 0
    for i in range(9):
        sum += (10-i) * (ord(S[i]) - 48)

    sum = (1100 - sum) % 11
    if sum!=10 and S[9] != chr(sum + 48):
        print("invalid")
        continue

    if sum==10 and S[9] != 'X':
        print("invalid")
        continue


    #Code to generate ISBN-13: Assume correct
    ans = "978-" + s
    sum = 8
    for i in range(9):
        sum += (3 - 2*(i%2)) * (ord(S[i]) - 48)

    sum = (1000 - sum) % 10
    ans = ans[:-1] + chr(sum + 48)
    print(ans)


    