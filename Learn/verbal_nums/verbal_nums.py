class VerbalRecognizer:
    def __init__(self, in_verbal: "str with verbal number"):
        self.in_verbal = in_verbal
        self.nums_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
                          'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
                          'fourty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'hundreds': 100, 'thousand': 1000, 'thousands': 1000,
                          'million': 1000000, 'millions': 1000000}

    def recognize(self) -> int:
        words = self.in_verbal.split(' ')
        numbers = list()
        result = 0
        for word in words:
            if (self.nums_dict.get(word, -1) != -1):
                numbers.append(self.nums_dict.get(word))

        temp_res = 0

        for num in numbers:
            if (num == 100):
                temp_res *= 100
            elif (num > 100):
                temp_res *= num
                result += temp_res
                temp_res = 0
            else:
                temp_res += num
        result += temp_res
        return result

recognizer = VerbalRecognizer(input("Enter number string: "))
print(recognizer.recognize())