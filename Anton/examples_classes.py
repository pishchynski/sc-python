class TestClass:
    name = "Class TestClass"

    def set(self, n):
        self.nickname = n

    def get(self):
        print("Nickname =", self.nickname)

    def __init__(self, n):
        self.set(n)
        print("INITIALIZATION")
        self.get()

    def __del__(self):
        print("DELETING")


def outer_method():
    print("Method is now in the class")


test = TestClass("Green")
print("Green NAME =", test.name)

red = TestClass("Red")
print("Red NAME =", red.name)

TestClass.name = "CHANGED NAME"

print("Red NAME =", red.name)
print("Green NAME =", test.name)

red.name = "CHANGED RED NAME"

print("Red NAME =", red.name)
print("Green NAME =", test.name)

del test
del red

print("Program END")


class Empty:
    pass


empty1 = Empty()
empty1.field = "FIELD"

print(empty1.field)

empty2 = Empty()
empty2.field = 234

print(empty2.field)

Empty.field = True

print(empty2.field)

del empty2.field

print(empty2.field)

del Empty.field

try:
    print(empty2.field)
except:
    print("empty2 has no fields with name 'field'")


class SpeakClass:
    def speak(self):
        print("Hi There")

obj = SpeakClass()
obj.speak()

SpeakClass.speak(obj)
SpeakClass.speak("Random text")



