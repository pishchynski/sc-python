from Anton.guesser import Guesser


class FaultGuesser(Guesser):
    """Guesser with a fault"""

    def __init__(self, number_to_guess, optimal_guess_count, fault):
        super().__init__(number_to_guess, optimal_guess_count)
        self.fault = fault

    def __print_fault_results(self, times_to_guess):
        fault_border = self.optimal_guess_count - self.fault

        if times_to_guess < fault_border:
            print("But you are far from fault border")
        elif times_to_guess == fault_border:
            print("And you are on the fault border!")
        else:
            print("And you managed to stay in fault border! Well Done!")

    def guess(self):
        times_to_guess = Guesser.guess(self)
        self.__print_fault_results(times_to_guess)
