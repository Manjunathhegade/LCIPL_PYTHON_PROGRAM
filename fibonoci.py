a=1
b=1

count = 0
while count < 12:
    a = a + b
    b = a + b
    if a % 2 == 0:
        print(a)
        count = count + 1
    if b % 2 == 0:
        print(b)
        count = count + 1
