
a = int(input())
i=0
for i in range(a):
    word = list(map(str, input().split()))
    if len(word[0]) == 5:
        print("3")
    else:
        if word[0][:-1]=="on" or word[0][1:]=="ne" or word[0][0]+word[0][-1]=="oe":
            print(1)
        else:
            print(2)


