import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 10, 100)
b = np.log(a)
# plt.plot(a, b)

x = np.random.normal(size=200)
# plt.hist(x, bins=30)

k = np.random.rand(100)
l = np.random.rand(100)
# plt.scatter(k, l)

r = np.arange(0, 3.0, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, projection="polar")
ax.plot(theta, r, color="r", linewidth=3)
ax.set_rmax(2.0) 


plt.show()