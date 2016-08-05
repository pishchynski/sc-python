from guesser import Guesser

class BoundsGuesser(Guesser):
    def __init__(self, user_number, min_attempts, max_attempts):
        self.user_number = user_number
        self.min_attempts = min_attempts
        self.max_attempts = max_attempts

    def min_attempts_check(self) -> bool:
        if (self.attempts < self.min_attempts):
            return False
        else:
            return True

    def guess(self):
        self.guess_user_number()
        while (not self.min_attempts_check()):
            self.guess_user_number()

number = int(input("Select number in [1..100] range: "))
min_attempts = int(input("Select min number of attempts: "))
max_attempts = int(input("Select max number of attempts: "))

guesser = BoundsGuesser(number, min_attempts, max_attempts)
guesser.guess()
print("Guessed number: ", guesser.get_guessed_number())
print("Attempts: ", guesser.get_attempts())