n = int(input())

for _ in range(n):
    number = int(input())
    b1 = bin(number).count('1')             # b1: count the number of ones

    M_hex = int(str(number), 16)
    b2 = bin(M_hex).count('1')              # b2: count the number of ones

    print(b1, b2)
    

