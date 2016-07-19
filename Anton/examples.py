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

z = 3
x = z
c = 4

print(z is x)
print(z is z)
print(x is z)
print(c is z)

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

n = 100
s = 0

for i in range(n + 1):
    s += i

print(s)

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
