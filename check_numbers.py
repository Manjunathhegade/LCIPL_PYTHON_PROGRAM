def check(num1, num2):
    if num1 >9 and num1 < 100:
        print(num1,"this number is two digit")
    elif num1 >99 and num1 < 1000:
        print(num1,"this number is three digit")
    else:
        print(num1)

    if num2 >9 and num2 < 100:
        print(num2,"this number is two digit")
    elif num2 >99 and num2 < 1000:
        print(num2,"this number is three digit")
    else:
        print(num2)

check(int(input("enter num1\n")),int(input("enter num2\n")))
        
