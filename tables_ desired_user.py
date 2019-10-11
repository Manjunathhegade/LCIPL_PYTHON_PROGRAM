def table(number):
    for i in range(1,11):
        total = number * i
        print(number, "*", i, "=",total)

x=table(int(input("enter number for multiplication\n")))
