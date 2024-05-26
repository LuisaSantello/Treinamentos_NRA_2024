import numpy as np

tupla = tuple(np.random.rand(5)*10)
print(tupla, '\nMaior valor da tupla: {}\nMenor valor da tupla: {}\n'.format(max(tupla), min(tupla)))