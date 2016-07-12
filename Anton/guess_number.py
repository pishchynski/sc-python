from Anton.guesser import Guesser

input_number = int(input("Enter your number: "))

guesser = Guesser(input_number, 15)
guesser.guess()
