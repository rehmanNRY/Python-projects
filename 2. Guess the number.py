# Guess the number from 0 to 100
import random
number = random.randint(0, 100)
print(number)
print("********** Choose a number **********")
user_nmbr = int(input("==> Enter the gusssed number: "))
guesses = 1
if user_nmbr == number:
    print(f"==> Number matches! You Win in {guesses} Turn")
else:
    while user_nmbr != number:
        while user_nmbr < 0 or user_nmbr > 100:
            print("********** Choose again **********")
            print("==> Choose number in range 0 - 100")
            user_nmbr = int(input("==> Enter the guessed number: "))
        print("********** Choose again **********")
        if user_nmbr < number:
            print("==> Too low, guess higher")
        else:
            print("==> Too high, guess lower")
        user_nmbr = int(input("==> Enter the guessed number: "))
        guesses += 1
    print(f"==> Number matches! You Win! in {guesses} Turns")