print(1 + 1)
print('Hi!')
print('a' + 'b', 'c')
a = 1
b = 123
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print('a' * 3)

expr = "1 + 32//3"

print(expr, "=", eval(expr))

print("LOGIC:")

print(1 and 2)
print(1 and 0)
print(not 0)
print(not 2)

print("IS:")

print(1 if 8 else 123)

# result = eval(input("Enter smth: "))
#
# if type(result) == int:
#     print("You entered an integer!")
# else:
#     print("This is not an integer :(")

a = 38

while a > 34:
    print("Decing number")
    a -= 1
    if a == 35:
        break
else:
    print("Already deced")

for c in "Python":
    print(c)
else:
    print("END")

try:
    (1 / 1)
except:
    print("Error!")
else:
    print("Everything is good")
finally:
    print("Code evaled")


def func(value, txt="Default text"):
    print("Value =", value)
    print(txt)


func(23)
func("My Text")

func(txt='3', value=213)


def my_sum(*numbers):
    summ = 0
    for number in numbers:
        summ += number
    return summ


print(my_sum(1, 2, 99))


def first_func(txt):
    print("First func:", txt)


my_func = first_func

my_func("Testing")


def solve_eq(f, x0, n):
    res = x0
    for k in range(1, n + 1):
        res = f(res)
    return res


def eq_1(x1):
    return x1 ** 2 - 5


def eq_2(x2):
    return (6 * x2 - 5) ** 0.5


x = solve_eq(eq_1, 0, 10)
print("First equation:", x)
x = solve_eq(eq_2, 4, 10)
print("Second equation:", x)


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 16):
    print("Fib", i, "=", fib(i), end=" ")

print()


def find_value(f, x):
    print("x =", x, " f(x) =", f(x))


find_value(lambda x=9: 1 / (1 + x ** 2), 2.0)

