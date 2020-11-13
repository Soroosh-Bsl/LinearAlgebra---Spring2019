import numpy as np
"Inputs are: Matrix's SVD which includes U, S, and V_T"
"Output is the best K rank approximation"

print("Enter Matric Dimensions :")
print("m = ", end='')
m = int(input())
print("n = ", end='')
n = int(input())

U = []
S = []
V_T = []


print("Enter K (approximation rank: ")
print("K = ", end='')
K = int(input())

print("Enter U: ")
for i in range(m):
    U.append(list(map(int, input().split())))
U = np.asmatrix(U)

print("Enter S: ")
for i in range(m):
    S.append(list(map(int, input().split())))
for i in range(min(m, n) - 1, K - 1, -1):
    S[i][i] = 0
S = np.asmatrix(S)

print("Enter V_T: ")
for i in range(n):
    V_T.append(list(map(int, input().split())))
V_T = np.asmatrix(V_T)

Matrix = np.matmul(np.matmul(U, S), V_T)
print(*Matrix)
