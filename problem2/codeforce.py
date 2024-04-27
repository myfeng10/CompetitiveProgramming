
while True:
    n = int(input())
    if n == 0:
        break
    binary = int(input())
    a=0
    b=0
    count = 1
    for i in range(32):
        if binary & 1<<i:
            if count %2==0:
                a+= 1<<i
            else:
                b+=1<<i
    print(a,b)
    # binary = list(str(bin(n)[2:]))
    # count = 1
    # an = ["0"]*len(binary)
    # bn = ["0"]*len(binary)
    # for i in range(len(binary)-1,-1,-1):
    #     if binary[i] == "1":
    #         if count % 2==0:
    #             bn[i]="1"
    #         else:
    #             an[i] = "1"
    #         count+=1
    # an = int("".join(an),2)
    # bn = int("".join(bn),2)
    # print(an,bn)
