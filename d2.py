

correct= input()
s = input()

plusCount = s.count("+")
minusCount = s.count("-")
quesCount = s.count("?")
sCurrent = plusCount - minusCount

finalLoc = correct.count("+")-correct.count("-")

stepLeft = finalLoc - sCurrent



if quesCount ==0:
    print(1)
else:
    numCorrect = result.count(finalLoc)
    print(numCorrect/len(result))


