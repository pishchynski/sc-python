nums = [1, 2, 3]
chars = list("Python")
pows = [2 ** i for i in range(20) if i % 4 == 2]

print(pows)
print(pows[1])
print(pows[-3])
print(pows[2:5])
print(pows[:3])
print(pows[3:])
print("Len=", len(pows))

test_list = [10, 20, 30]
test_sub_list = test_list[1:2]

print(test_list)
print(test_sub_list)

test_sub_list[0] = 999

print(test_list)
print(test_sub_list)

print([1, 2, 3][::-1])

test_list = [8, 9, 10, 20]

print(test_list)

test_list[1:3] = []

print(test_list)

b = tuple([1, 2, 3])

print(b)

c = tuple("C++")

print(c)

a = b + c

print(a)

