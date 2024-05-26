import numpy as np

A = np.random.rand(3,3)*9
B = np.random.rand(3,3)*9

print(A)
print(B)

C = A + B 

print(C)

D = A * B

print(D)

E = A @ B

print(E)