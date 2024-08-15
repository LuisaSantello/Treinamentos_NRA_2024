import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(0, 11, 6)
#a =np.linspace(-10,20, 10)
b = a**3

plt.title('Função cúbica')
plt.grid(True)
plt.xlabel('Variáveis')
plt.ylabel('elevadas ao cubo')
plt.plot(a, b, marker ='o', label='a**3')
plt.legend()
plt.show()