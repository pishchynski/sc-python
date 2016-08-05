from random import randint

class Guesser:
    """Class Guesser guesses the number defined by user"""

    def __init__(self, user_number, max_attempts):
        self.user_number = user_number
        self.max_attempts = max_attempts

    def set_user_number(self, user_number: "int number that is to guess"):
        self.user_number = user_number

    def guess_user_number(self):
        count = 0
        while (count > self.max_attempts) or (count == 0):
            count = 0
            count += 1
            guessed_number = randint(1, 100)
            while (guessed_number != self.user_number and count <= self.max_attempts):
                guessed_number = randint(1, 100)
                count += 1
            self.attempts = count
            self.guessed_number = guessed_number

    def get_guessed_number(self) -> int:
        return self.guessed_number

    def get_attempts(self) -> int:
        return self.attempts

    def guess(self):
        self.guess_user_number()