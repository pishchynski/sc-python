import random

var = int(input("Enter your number: "))
print("Your number is: ", var)

times_to_guess = 0
guessed_number = -1

while guessed_number != var:
    guessed_number = random.randrange(0, var + 1)
    times_to_guess += 1

print("It took", times_to_guess, "guesses to find your number")
