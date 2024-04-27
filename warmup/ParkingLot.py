

keyboardIn = []
num = -1
count=0
while True:
    if count == (int(num)*2):
        break
    line = input()
  
    content = line.split()
    content = [int(x) for x in content]
    if num == -1:
        num = content[0]
        continue
      
    keyboardIn.append(content)
    count +=1

i = 0
while i < len(keyboardIn):
    #print("current line",keyboardIn[i], keyboardIn[i+1])
    minimum = min(keyboardIn[i+1])
    maximum = max(keyboardIn[i+1])
    i+=2
    print((maximum-minimum)*2)

