from Anton.fault_guesser import FaultGuesser

input_number = int(input("Enter your number: "))

guesser = FaultGuesser(input_number, 15, 3)
guesser.guess()
