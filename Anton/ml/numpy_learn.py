import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex)
print(b)

print()

print(np.zeros((3, 5)))

print()

print(np.ones((2, 2, 2)))

print()

print(np.eye(5))

print()

print(np.arange(0, 1, 0.1))

print()

print(np.linspace(1, 5, 9))


def f1(i, j):
    print("i:", i)
    print("j:", j)
    return 3 * i + j

np.fromfunction(f1, (3, 3))

print(np.arange(0, 3000, 1))
