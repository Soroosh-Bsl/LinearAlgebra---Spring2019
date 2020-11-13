import numpy as np
from math import hypot


# This function finds the QR Decomposition

def qr_decomposition(matrix):
    r = np.copy(matrix)
    (n_rows, n_cols) = np.shape(matrix)
    (rows, cols) = np.tril_indices(n_rows, -1, n_cols)

    q = np.identity(n_rows)

    for (row, col) in zip(rows, cols):
        if not r[row, col] == 0:
            (c, s) = find_rotation(r[col, col], r[row, col])
            rot = np.identity(n_rows)
            rot[row, col] = s
            rot[col, row] = -s
            rot[[col, row], [col, row]] = c

            r = np.dot(rot, r)
            q = np.dot(q, rot.T)

    return q, r


def find_rotation(x1, x2):
    l = hypot(x1, x2)
    c = x1/l
    s = -x2/l

    return c, s


# Getting Input and do the calculations

print("Insert dimensions of A: n m (n < m)")
n, m = map(int, input().split())
A = [[0 for i in range(m)] for j in range(n)]
print("Insert A:")
for i in range(n):
    A[i] = list(map(int, input().split()))
A = np.array(A)
print("Insert b:")
b = np.array(list(map(int, input().split())))

(q, r) = qr_decomposition(A.T)
(m, n) = np.shape(A)
print("Q:")
print(q)
print("R:")
print(r)
r_tilda = r[0:m][0:m]
x = np.dot(q[:, 0:m], np.linalg.inv(r_tilda.T))
x = np.dot(x, b)
print("Minimum answer is :")
print(x)
