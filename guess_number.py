secret_number=9
count_guess=0
count_limit=3
while count_guess<count_limit:
    guess=input("guess  ")
    count_guess  += 1
    if guess == secret_number:
        print("you win!")
    elif guess != secret_number:
        print("try again")
else:
    print("you lose!")