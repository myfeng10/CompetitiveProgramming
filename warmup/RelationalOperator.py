

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
    first = int(value[0])
    second = int(value[1])
    if first < second:
        print("<")
    elif first > second:  
        print(">")
    else:
        print("=")