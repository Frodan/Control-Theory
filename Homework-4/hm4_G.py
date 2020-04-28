import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy as sp


A = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 2.28, 0, 0],
              [0, 21.21, 0, 0]])

B = np.array([[0],
              [0],
              [1/11.6],
              [1/8.151]])

Q = np.array([[1000, 0, 0, 0],
              [0, 1000, 0, 0],
              [0, 0, 1000, 0],
              [0, 0, 0, 1000]])

R = np.array([[5]])

S = sp.linalg.solve_continuous_are(A, B, Q, R)

K = np.linalg.inv(R).dot(np.transpose(B).dot(S))


def next(x, t):
  x_norm = np.transpose(x)
  AsubBK = A - B.dot(K)
  return np.transpose(AsubBK.dot(x_norm))


time = np.linspace(0, 100, 1000)

x0 = [1, 2, 3, 4]
solution = odeint(next, x0, time)
plt.plot(time, solution[:,0])
plt.show()
