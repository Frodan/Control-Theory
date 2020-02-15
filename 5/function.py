import numpy as np


def to_ss(coefficients, b0):
    coefficients = np.array(coefficients)
    degree = len(coefficients) # degree of the polynomial

    normalized = coefficients[1:] / coefficients[0] # divide by "ak"

    A = np.zeros((degree-1, degree-1))  # state matrix
    A[0, 0:] = -normalized
    A[1:, 0:(degree-2)] = np.eye(degree-2)

    A = np.flip(A)

    B = np.zeros((degree - 1, 1))
    B[-1][0] = b0
    return A, B


if __name__ == "__main__":
    A, B = to_ss([1, -1, -2], 4)
    print("matrix A:")
    print(A)
    print("matrix B:")
    print(B)
