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


class ComplexNum:
    def __init__(self, x=0, y=0):

        if type(x) == ComplexNum:
            self.Re = x.Re
            self.Im = x.Im
        else:
            self.Re = x
            self.Im = y

    def show(self):
        print("Re =", self.Re)
        print("Im =", self.Im)


a = ComplexNum(1, 2)
b = ComplexNum(a)

print("\nNumber a:")
a.show()

print("Number b:")
b.show()

print("CHANGING a")
a.Re = 20
a.Im = 20

print("Number a:")
a.show()

print("Number b:")
b.show()


class BoxSize:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def show(self):
        print("Box size and volume:")
        print("Width:", self.width)
        print("Height:", self.height)
        print("Depth:", self.depth)
        print("Volume:", self.volume())


class BoxParams:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def show(self):
        print("Extra box params:")
        print("Weight:", self.weight)
        print("Color:", self.color)


class Box(BoxSize, BoxParams):
    def __init__(self, width, height, depth, weight, color):
        BoxSize.__init__(self, width, height, depth)
        BoxParams.__init__(self, weight, color)
        self.show()

    def show(self):
        BoxParams.show(self)
        print()
        BoxSize.show(self)

print("\n")
box = Box(10, 20, 30, 5, "Красная")

print(object.__doc__)
print(Box.__mro__)
print(Box.__qualname__)
