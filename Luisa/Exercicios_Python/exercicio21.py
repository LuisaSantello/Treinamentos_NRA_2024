import numpy as np
import random


a = np.random.randint(0, 10, (3, 3))
print(a)
b = np.random.randint(0,10,(3, 3))
print(b)
c = a + b
print(c)
d = a*b
print(d)
e = a@b
print(e)