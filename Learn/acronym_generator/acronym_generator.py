class AcronymGenerator:
    """Generates acronym from any sequence of words"""
    def __parse(self, line: "str to parse to list") -> list:
        return line.split()

    def generate(self, line="", *args: "str with phrase to acronymize, phrase to acronymize splitted to words") -> str:
        if (line != ""):
            words = [word for word in self.__parse(line)]
            words.append(list(args))
        else:
            words = list(args)


        letter = lambda str: str[0]
        result = ""
        for word in words:
            result += letter(word)
        result = result.upper()
        return result

phrase = input("input phrase to make acronym: ")
generator = AcronymGenerator()
print(generator.generate('soft', 'club', line = phrase))