import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


A = np.array([[0, 1], [-15, -63]])

B = np.array([0, 1])

k_p = 1500
k_d = 10
K = np.array([k_p, k_d])
e, v = np.linalg.eig(A - B.reshape(2, 1).dot(K.reshape(1, 2)))
print("eigenvalues of A - BK:", e)

print("A: \n", A, end='\n\n')
print("B: \n", B, end='\n\n')
print("K: \n", K, end='\n\n')

time = np.linspace(0, 10, 200)

def x_desired(t):
    return np.array([0]) if t < 1 else np.array([1])

#def x_desired(t):
#    return np.array([np.sin(t)])

#def x_desired(t):
#  return np.array([t*t])

def next(x, t):
  e = x_desired(t) - x
  K1 = K.dot(e)
  return A.dot(x) + B.dot(K1)

x0 = [0, 0]
x = odeint(next, x0, time)

desired_path = [x_desired(t1)[0] for t1 in time]

plt.plot(time, x[:,0], label="PD controller")
plt.plot(time, desired_path, label="Desired")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


plt.show()