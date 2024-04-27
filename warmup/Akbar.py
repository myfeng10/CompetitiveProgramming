count=1
while True:
    n = input()
    if n == "*":
        break
    if n == "Hajj":
        print("Case",str(count)+":","Hajj-e-Akbar")
    else:
        print("Case",str(count)+":","Hajj-e-Asghar")
    count+=1