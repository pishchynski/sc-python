def show(*args):
    i = 0
    for arg in args:
        i += 1
        print(i, ") ", arg, sep="")
    print("END")

show()
show(100)
show([1, 2, 3])
show(*[1, 2, 3])
show("String1", "String2")
