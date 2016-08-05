from learn_app.acronym_generator import acronym_generator as ag
from number_guesser.bounds_guesser import BoundsGuesser
from verbal_nums.verbal_nums import VerbalRecognizer


if __name__ == '__main__':
    selection = 4
    while(True):
        print("Select script to be run: ")
        print("1. Acronym generator ")
        print("2. Number guesser")
        print("3. Verbal numbers recognizer")
        print("0. Exit")
        selection = int(input())
        if (selection == 1):
            acronym_generator = ag.AcronymGenerator()
        elif (selection == 2):
            number_guesser = BoundsGuesser()
        elif (selection == 3):
            number_recognizer = VerbalRecognizer()
        elif (selection == 0):
            break