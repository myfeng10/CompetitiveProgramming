

keyboardIn = []
num = -1
count=0
while True:
    # reset num
    if count == (int(num)+1):
        num=-1
        count=0
 
    line = input()
  
    content = line.split()
    content = [int(x) for x in content]

    if content[0] == 0 and len(content) == 1:
        break 

    if num == -1:
        num = content[0]
        keyboardIn.append(content)
       
        continue
    
    if count == 0:
        keyboardIn[-1].append(content)
        count+=1
        continue
    keyboardIn[-1].append(content)
    count +=1

for value in keyboardIn:
    num = value[0]
    x,y = value[1]
    #print("num",num)
    #print("division",x,y)
    for i in range(2,len(value)):
        c_x,c_y = value[i]
        #print("corrdinate:",value[i])
        if c_x > x and c_y > y:
            print("NE")
        elif c_x > x and c_y < y:
            print("SE")
        elif c_x < x and c_y > y:
            print("NO")
        elif c_x < x and c_y < y:
            print("SO")
        else:
            print("divisa")
            
         