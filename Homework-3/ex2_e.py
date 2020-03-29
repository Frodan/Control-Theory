import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


A = np.array([[0, 1], [-15, -63]])

B = np.array([0, 1])

k_p = 9000
k_d = 110
k_i = 0.3
K = np.array([k_p, k_d])

e, v = np.linalg.eig(A - B.reshape(2, 1).dot(K.reshape(1, 2)))
print("eigenvalues of A - BK:", e)

print("A: \n", A, end='\n\n')
print("B: \n", B, end='\n\n')
print("K: \n", K, end='\n\n')

time = np.linspace(0, 10, 200)

errors = {}
for t in time:
  errors[t] = 0


def x_desired(t):
  return np.array([t**2])


def next(x, t):
  e = x_desired(t) - x
  if t in errors.keys():
    if errors[t] != 0:
      errors[t] = (errors[t] + e[0])/2
    else:
      errors[t] = e[0]
  else:
    min = 1000
    t_min = 0
    for t1 in time:
      if abs(t - t1) < min:
        min = abs(t - t1)
        t_min = t1
    if errors[t_min] != 0:
      errors[t_min] = (errors[t_min] + e[0])/2
    else:
      errors[t_min] = e[0]
  total_error = 0
  for t1 in time:
    if t1 < t:
      total_error += errors[t1]
  K1 = K.dot(e) + k_i*total_error - 9.8
  return A.dot(x) + B.dot(K1)

x0 = [0, 0]
x = odeint(next, x0, time)

desired_path = [x_desired(t1)[0] for t1 in time]

plt.plot(time, x[:,0], label="PID Controller")
plt.plot(time, desired_path, label="Desired")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()