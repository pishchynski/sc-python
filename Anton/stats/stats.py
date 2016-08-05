import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.ylim([-1.0, 1.0])
plt.xlim([-3, 3])

figure.savefig('sine_wave_plot.svg')