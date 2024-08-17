import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 4, 5, 6]

plt.plot(x, y, marker='o', linestyle='dotted')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Titulo do gráfico')
plt.grid(True)
plt.show()
