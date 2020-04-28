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

C = np.array([[1, 0, 0, 0],
              [0, 0, 0, 0]])

Q = np.array([[100, 0, 0, 0],
              [0, 100, 0, 0],
              [0, 0, 100, 0],
              [0, 0, 0, 100]])

R = np.array([[1, 0],
              [0, 1]])

A_transpose = np.transpose(A)
C_transpose = np.transpose(C)

S = sp.linalg.solve_continuous_are(A_transpose, C_transpose, Q, R)

L = np.transpose(np.linalg.inv(R).dot(np.transpose(C_transpose).dot(S)))

def next(x, t):
  x_norm = np.transpose(x)
  AsubBK = A - L.dot(C)
  return np.transpose(AsubBK.dot(x_norm))

time = np.linspace(0, 100, 1000)

x0 = [10, 10, 10, 10]
solution = odeint(next, x0, time)
plt.xlabel('x')
plt.ylabel('time')
plt.plot(time, solution[:,0])
plt.show()