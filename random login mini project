random_number = int(input("choose a random number between 1 to 25\n"))
count = 0
while count < 5:
    login_id = int(input("enter your login ID\n"))
    guess_no = random_number - login_id
    if random_number == login_id:
        print("Welcome")
        break
    elif guess_no < 3 and guess_no > -3:
        print("InVaLiD paSsCoDe")
        count=count+1
    elif guess_no >= 3:
        print("invalid passcode")
        count=count+1
    elif guess_no <= -3:
        print("INVALID PASSCODE")
        count=count+1

if count == 5:
    print("Login FAILED!!!")
        
