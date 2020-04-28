import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy as sp
import scipy.signal as signal
import control

A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 5.92, 0, 0],
              [0, 22.65, 0, 0]])

B = np.array([[0],
              [0],
              [1/5.3],
              [1/9.775]])

C = np.array([[1, 0, 0, 0]])

P = np.array([-5, -6, -7, -8])

A_transpose = np.transpose(A)
C_transpose = np.transpose(C)

control1 = signal.place_poles(A_transpose, C_transpose, P)

L = np.transpose(control1.gain_matrix)

def f(x, t):
  x_temp = np.transpose(x)
  controlled = A - L.dot(C)
  return np.transpose(controlled.dot(x_temp))
  #return np.transpose(A.dot(x_temp))

time = np.linspace(0, 100, 1000)
x0 = np.array([10, 10, 10, 10])
solution = odeint(f, x0, time)
plt.xlabel('x')
plt.ylabel('time')
plt.plot(time, solution[:,0])
plt.show()