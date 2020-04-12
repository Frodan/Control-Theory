import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 2.28, 0, 0],
              [0, 21.21, 0, 0]])

B = np.array([[0],
              [0],
              [1/11.6],
              [1/8.151]])

P = np.array([-1, -2, -3, -4])

control = signal.place_poles(A, B, P)

def f(x, t):
  x_norm = np.transpose(x)
  controlled = A - B.dot(control.gain_matrix)
  return np.transpose(controlled.dot(x_norm))


time = np.linspace(0, 100, 1000)
x0 = np.array([-5, -6, -7, -8])
solution = odeint(f, x0, time)
plt.xlabel('x')
plt.ylabel('time')
plt.plot(time, solution[:,0])
plt.show()

