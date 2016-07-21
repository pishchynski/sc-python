from math import exp, sin, cos, tan


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


def F(f):
    return lambda x: exp(-f(x) ** 2)


def Q(f):
    def q(x):
        return tan(f(x))

    return q


@F
def f(x):
    return sin(x)


@F
def g(x):
    return cos(x)


@Q
@F
def h(x):
    return x


n = 5
print("\nf(x):")
for i in range(n + 1):
    z = i / n
    print(f(z), "->", exp(-sin(z) ** 2))

print("\nh(x):")
for i in range(n + 1):
    z = i / n
    print(h(z), "->", tan(exp(-z ** 2)))
