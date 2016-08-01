import numpy as np
import theano.tensor as T
from theano import function
from theano import pp
from theano import shared

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

state = shared(0)
inc = T.iscalar('inc')

accumulator = function([inc], state, updates=[(state, state + inc)])
decrementor = function([inc], state, updates=[(state, state - inc)])

print()
print(state.get_value())
accumulator(1)
print(state.get_value())
accumulator(300)
print(state.get_value())
decrementor(2)
print(state.get_value())


print()
print()
print()

rng = np.random

N = 400
feats = 784

D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))
training_steps = 10000

x = T.matrix('x')
y = T.matrix('y')

w = shared(rng.randn(feats), name='w')

b = shared(0., name='b')

print("Initial model:")
print(w.get_value())
print(b.get_value())

p_1 = 1 / (1 + T.exp(-T.dot(x,w) - b))
prediction = p_1 > 0.5
xent = -y * T.log(p_1) - (1 - y) * T.log(1 - p_1)
cost = xent.mean() + 0.01 * (w ** 2).sum()

gw, gb = T.grad(cost, [w, b])

train = function(
          inputs=[x,y],
          outputs=[prediction, xent],
          updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)))

predict = function(inputs=[x], outputs=prediction)

for i in range(training_steps):
    pred, err = train(D[0], D[1])

print("Final model:")
print(w.get_value())
print(b.get_value())
print("target values for D:")
print(D[1])
print("prediction on D:")
print(predict(D[0]))