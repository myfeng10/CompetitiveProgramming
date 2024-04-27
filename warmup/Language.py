keyboardIn = []
while True:
    content = input()
    if content == "#":
        break
    keyboardIn.append(content)

count = 1
for value in keyboardIn:
    if value == 'HELLO':
        print("Case",str(count)+":","ENGLISH")
    elif value == "HOLA":
        print("Case",str(count)+":","SPANISH")
    elif value == "HALLO":
        print("Case",str(count)+":","GERMAN")
    elif value == "BONJOUR":
        print("Case",str(count)+":","FRENCH")
    elif value == "CIAO":
        print("Case",str(count)+":","ITALIAN")
    elif value == "ZDRAVSTVUJTE":
        print("Case",str(count)+":","RUSSIAN")
    else:
        print("Case",str(count)+":","UNKNOWN")
    count+=1
