class TestClass:
    def __init__(self):
        print("INITIALIZATION")

    def __del__(self):
        print("DELETING")


def outer_method():
    print("Method is now in the class")


test = TestClass()
test.prt = outer_method

test.prt()

del test

print("AFTER")

