from random import randint

class Guesser:
    """Class Guesser guesses the number defined by user"""

    def __init__(self, user_number):
        self.user_number = user_number

    def set_user_number(self, user_number: "int number that is to guess"):
        self.user_number = user_number

    def guess_user_number(self):
        count = 1
        self.guessed_number = randint(1, 10)
        while(self.guessed_number != self.user_number):
            self.guessed_number = randint(1, 10)
            count += 1
        self.attempts = count

    def get_guessed_number(self) -> int:
        return self.guessed_number

    def get_attempts(self) -> int:
        return self.attempts


number = int(input("Select number in [1..10] range: "))

guesser = Guesser(number)
guesser.guess_user_number()
print("Guessed number: ", guesser.get_guessed_number())
print("Attempts: ", guesser.get_attempts())