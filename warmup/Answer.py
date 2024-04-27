keyboardIn = []
count = 0
num = -1
while True:
    if count == int(num):
        break
    line = input()
    content = int(line.split()[0])
    if num == -1:
        num = content
        continue
    keyboardIn.append(content)
    count +=1


for value in keyboardIn:
    answer =int((((value * 567 / 9) + 7492) * 235 / 47 - 498)/10)
    #print(answer)
    print(str(answer)[-1])