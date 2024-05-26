import numpy as np
import matplotlib.pyplot as plt

dados_x1 = np.random.rand(5)
dados_y1 = np.random.rand(5)
dados_x2 = np.random.rand(5)
dados_y2 = np.random.rand(5)

plt.style.use('fivethirtyeight')
fig, graf = plt.subplots(figsize = (14,9))
plt.rcParams.update({"text.usetex": True})
graf.set(title='Titulo do gráfico', xlabel = 'Eixo_x', ylabel = 'Eixo_y')
graf.plot(dados_x1, dados_y1, dados_x2, dados_y2)
graf.legend([r'$\alpha$', r'$\beta$'])
plt.show()