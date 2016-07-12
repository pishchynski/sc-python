import random


def guess_func(number_to_guess, times_to_guess, optimal_guess_count):
    print("Your number is:", number_to_guess)
    while (times_to_guess > optimal_guess_count) or (times_to_guess == 0):
        times_to_guess = 0
        guessed_number = -1
        while guessed_number != number_to_guess:
            guessed_number = random.randrange(0, number_to_guess + 1)
            times_to_guess += 1

    print("It took", times_to_guess, "guesses to find your number")
    print("Optimal guesses count =", optimal_guess_count)

    if times_to_guess == optimal_guess_count:
        print("You were on an optimal border")
    else:
        print("Better than expected!")
