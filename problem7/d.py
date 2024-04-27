
def generate_binary_combinations(n):
    result = []
    for i in range(2 ** n):
        binary_format = format(i, f'0{n}b')
        result.append(binary_format)
    return result
        
correct= input()
s = input()

plusCount = s.count("+")
minusCount = s.count("-")
quesCount = s.count("?")
sCurrent = plusCount - minusCount

finalLoc = correct.count("+")-correct.count("-")
# print("finalLoc",finalLoc, "sCurrent", sCurrent)
stepLeft = finalLoc - sCurrent
# print("stepLeft",stepLeft)

bincomb = generate_binary_combinations(quesCount)

result = []
for i in bincomb:
    temp = 0
    for ele in i:
        if ele == "0":
            temp -=1
        else:
            temp +=1
    result.append(temp)

# print(bincomb)
# print(result)

if quesCount ==0:
    if finalLoc == sCurrent:
        print(1)
    else:
        print(0)
else:
    # print(stepLeft)
    numCorrect = result.count(stepLeft)
    print(numCorrect/len(result))

