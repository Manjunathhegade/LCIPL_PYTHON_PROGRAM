def fibo(user_input):
    a = 1
    b = 1
    while True:
        if (a+b) <= user_input:
            a = a+b
            b = a+b
        else:
            break
    if user_input  == a or user_input == b:
        return "yes this number is fibonacci"
    dif1 = user_input - a
    dif2 = b - user_input
    if dif1 == dif2:
        return "nearest fibonacci numbers are "+str(a)+" and "+str(b)
    elif dif1 < dif2:
        return "nearest fibonacci number is "+str(a)
    else:
        return "nearest fibonacci number is "+str(b)

x = fibo(int(input("enter your number\n")))
print(x)
