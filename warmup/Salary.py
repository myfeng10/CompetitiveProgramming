keyboardIn = []
num = -1
count = 0 
while True:
    if count == int(num):
        break
    content = input()
    if num == -1:
        num = int(content)
        keyboardIn.append([num])
        continue
    content = content.split()
    content = [int(x) for x in content]
    keyboardIn[0].append(content)
    count+=1

i = 1
for value in keyboardIn[0][1:]:
    minimum = min(value)
    maximum = max(value)
    if value[0] != minimum and value[0] != maximum:
        middle = value[0]
    elif value[1] != minimum and value[1] != maximum:
        middle = value[1]
    else:
        middle = value[2]
    print("Case",str(i)+":",middle)
    i += 1