from learn_app.acronym_generator.acronym_generator import AcronymGenerator
from learn_app.number_guesser.bounds_guesser import BoundsGuesser
from learn_app.verbal_nums.verbal_nums import VerbalRecognizer

selection = 4
while(True):
    print("Select script to be run: ")
    print("1. Acronym generator ")
    print("2. Number guesser")
    print("3. Verbal numbers recognizer")
    print("0. Exit")
    selection = int(input())
    if (selection == 1):
        acronym_generator = AcronymGenerator()
    elif (selection == 2):
        number_guesser = BoundsGuesser()
    elif (selection == 3):
        number_recognizer = VerbalRecognizer()
    elif (selection == 0):
        break