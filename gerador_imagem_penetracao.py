import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados fornecidos
penetracao_path = 'assets/penetracao.txt'

# Dados (invertemos o eixo para atender a solicitação)
comprimento_cordao = np.arange(0, 111.5, 0.5)
penetracao = np.loadtxt(penetracao_path)

# Faixa de "quase furo"
limite_inferior = 0.25 * np.max(penetracao)
limite_superior = 0.80 * np.max(penetracao)

# Plot estático
plt.figure(figsize=(10, 6))
plt.plot(comprimento_cordao, penetracao, label='Penetração', color='blue')
plt.axhline(limite_inferior, color='red', linestyle='--', label='Limite Inferior (~25%)')
plt.axhline(limite_superior, color='green', linestyle='--', label='Limite Superior (~80%)')
plt.xlabel('Comprimento do Cordão (mm)')
plt.ylabel('Penetração (mm)')
plt.title('Curva de Penetração Invertida com Limites de "Quase Furo"')
plt.legend()
plt.grid()
plt.show()
plt.savefig('output/curva_penetracao_invertida.png', dpi=300)

# Código para gerar GIF
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, np.max(comprimento_cordao))
ax.set_ylim(0, 1.1 * np.max(penetracao))
ax.set_xlabel('Comprimento do Cordão (mm)')
ax.set_ylabel('Penetração (mm)')
ax.set_title('Evolução da Curva de Penetração')
line, = ax.plot([], [], color='blue')

# Função de atualização para o GIF
def update(frame):
    line.set_data(comprimento_cordao[:frame], penetracao[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(comprimento_cordao), interval=50, blit=True)

# Salvar o GIF
ani.save('output/evolucao_penetracao.gif', writer=PillowWriter(fps=10))

plt.show()
