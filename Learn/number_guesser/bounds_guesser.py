from guesser import Guesser

class BoundsGuesser(Guesser):
    def __init__(self, user_number, min_attempts, max_attempts):
        self.user_number = user_number
        self.min_attempts = min_attempts
        self.max_attempts = max_attempts

    def __init__(self):
        self.launch()

    def min_attempts_check(self) -> bool:
        if (self.attempts < self.min_attempts):
            return False
        else:
            return True

    def guess(self):
        self.guess_user_number()
        while (not self.min_attempts_check()):
            self.guess_user_number()

    def launch(self):
        self.user_number = int(input("Select number in [1..100] range: "))
        self.min_attempts = int(input("Select min number of attempts: "))
        self.max_attempts = int(input("Select max number of attempts: "))
        self.guess()
        print("Guessed number: ", self.get_guessed_number())
        print("Attempts: ", self.get_attempts())

guesser = BoundsGuesser()