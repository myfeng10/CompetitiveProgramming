import math

keyboardIn = []
num = -1
count=0
while True:
    if count == int(num):
        break
    line = input()
  

    content = line.split()
    if num == -1:
        num = content[0]
        continue
    
    keyboardIn.append(content)
    count +=1


for value in keyboardIn:
    n = int(value[0])
    m = int(value[1])
    n -= 2
    m -= 2

    print(math.ceil(n/3)*math.ceil(m/3))