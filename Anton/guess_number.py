import random

input_number = int(input("Enter your number: "))
print("Your number is:", input_number)

times_to_guess = 0
optimal_guess_count = 15

while (times_to_guess > optimal_guess_count) or (times_to_guess == 0):
    times_to_guess = 0
    guessed_number = -1
    while guessed_number != input_number:
        guessed_number = random.randrange(0, input_number + 1)
        times_to_guess += 1

print("It took", times_to_guess, "guesses to find your number")
print("Optimal guesses count =", optimal_guess_count)

if times_to_guess == optimal_guess_count:
    print("You were on an optimal border")
else:
    print("Better than expected!")
