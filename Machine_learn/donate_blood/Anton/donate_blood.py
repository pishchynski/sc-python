import numpy as np
import theano.tensor as T
from theano import function
from theano import pp

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y

f = function([x, y], z)

print(f(2, 3))
print(pp(z))

a = T.dmatrix('a')
b = T.dmatrix('b')
c = a + b

g = function([a, b], c)

print()
print(g([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print()

a = T.vector() # declare variable
b = T.vector() # declare variable
out = a ** 2 + b ** 2 + 2 * a * b               # build symbolic expression
f = function([a, b], out)   # compile function
print(f([0, 1, 2], [2, 1, 0]))

x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = function([x], s)
print(logistic([[0, 1], [-1, -2]]))

a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff ** 2
f = function([a, b], [diff, abs_diff, diff_squared] )
print()
print(f([[1, 1], [1, 1]], [[0, 1], [2, 3]]))