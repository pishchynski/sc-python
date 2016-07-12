import random


class Guesser:
    """Class for guessing numbers"""

    def __init__(self, number_to_guess, optimal_guess_count):
        self.number_to_guess = number_to_guess
        self.optimal_guess_count = optimal_guess_count

    def __guess_the_num(self):
        times_to_guess = 0
        while (times_to_guess > self.optimal_guess_count) or (times_to_guess == 0):
            times_to_guess = 0
            guessed_number = -1
            while guessed_number != self.number_to_guess:
                guessed_number = random.randrange(0, self.number_to_guess + 1)
                times_to_guess += 1
        return times_to_guess

    def __print_results(self, times_to_guess):
        print("It took", times_to_guess, "guesses to find your number")
        print("Optimal guesses count =", self.optimal_guess_count)

        if times_to_guess == self.optimal_guess_count:
            print("You were on an optimal border")
        else:
            print("Better than expected!")

    def guess(self):
        print("Your number is:", self.number_to_guess)

        times_to_guess = self.__guess_the_num()

        self.__print_results(times_to_guess)
