import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


def solve_ss(coefficients, initial_conds, b_func):
    global time
    coefficients = np.array(coefficients)
    degree = len(coefficients)
    normalized = coefficients[1:] / coefficients[0]

    A = np.zeros((degree - 1, degree - 1))
    A[0, 0:] = -normalized
    A[1:, 0:(degree - 2)] = np.eye(degree - 2)
    A = np.flip(A)

    def model(x, t):
        res = np.zeros(degree - 1)
        for i in range(len(res)):
            res[i] = 0
            for j in range(len(x)):
                res[i] += A[i][j] * x[j]

        res[-1] -= b_func(t)
        return res

    return odeint(model, initial_conds, time)


def solve_ode(coeffs, initial_conds, b_func):
    global time
    coeffs = np.array(coeffs)
    initial_conds = np.array(initial_conds)
    normalized = -(coeffs[1:] / coeffs[0])

    def model(x, t):
        u = b_func(t)
        sol = u
        for i in range(len(x)):
            sol += normalized[i] * x[i]
        result = np.append(x[1:], sol)
        return result

    return odeint(model, initial_conds, time)


if __name__ == "__main__":

    coeffs = np.array([1, -1, -2])
    initial_conds = np.array([5, 2])

    def b_func(t):
        return math.sin(2 * t) - 3


    time = np.linspace(0, 10, 100)

    ode = solve_ode(coeffs, initial_conds, b_func)
    ss = solve_ss(coeffs, initial_conds, b_func)
    solution = {"ODE": ode, "SS": ss}

    # ode based model
    plt.subplot(121)
    plt.title("ODE")
    plt.plot(time, solution["ODE"])
    plt.xlabel('time')
    plt.ylabel('x(t)')

    # state space based model
    plt.subplot(122)
    plt.title("SS")
    plt.plot(time, solution["SS"])
    plt.xlabel('time')
    plt.ylabel('x(t)')

    plt.show()
