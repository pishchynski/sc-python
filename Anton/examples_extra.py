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


def v_show(first, second, *args, **kwargs):
    print()
    print("First:", first)
    print("Second:", second)
    print("Args:", args)
    print("Kwargs:", kwargs)


print("\n")
v_show(10, 20, 30, 40, 50, 60, 70)
v_show(10, 20, 50, 60, 70, third=30, fourth=40)
v_show(10, 20, third=30, fourth=40)
v_show(second=20, first=10)
v_show(second=20, first=10, third=30)
