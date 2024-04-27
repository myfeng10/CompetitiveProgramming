keyboardIn = []
hasCount = False
while True:
    line = input()
    if line == "0":
        break
    content = line.split()
    if hasCount == False:
        keyboardIn.append(content)
        hasCount = True
        continue
    keyboardIn[-1].append(content)
    hasCount = False

count = 1
for value in keyboardIn:
    content = value[1]
    total = len(content)
    zeros = 0
    for x in content:
      
        if x == "0":
            zeros +=1
    print("Case",str(count)+":",(total-zeros) - zeros)
    count+=1