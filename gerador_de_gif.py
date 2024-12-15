from scipy.interpolate import UnivariateSpline
import numpy as np

from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
from matplotlib import rc

from IPython.display import HTML


# Dados fornecidos
penetracao_path = 'assets/penetracao.txt'

# Carregar dados dos arquivos
comprimento = np.arange(0, 111.5, 0.5)
penetracao = np.loadtxt(penetracao_path)

# Suavizando os dados
spl = UnivariateSpline(comprimento, penetracao, s=0.2)
comprimento_suavizado = np.linspace(min(comprimento), max(comprimento), 500)
penetracao_suavizada = spl(comprimento_suavizado)

# Configuração do GIF
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', lw=2, label="Penetração Suavizada")

ax.set_xlim(0, max(comprimento))
ax.set_ylim(5, 0)

ax.set_xlabel('Comprimento do Cordão')
ax.set_title('Progresso da Penetração')

# Faixa de referência (25% a 80% do valor máximo)
ref_min = 0.793
ref_max = 2.54

ref_band = ax.fill_between(
    x=comprimento,
    y1=ref_min,
    y2=ref_max,
    color='yellow',
    alpha=0.3,
    label='Faixa de referência'
)
legend = ax.legend(loc = 'lower right')


# Adicionando legenda personalizada
additional_legend = (
    "Aluno: João Borges\n"
    "Orientador: Rubelmar Neto\n"
    "Universidade do Estado do Amazonas"
)
plt.text(
    x=0.02, 
    y=0.05, 
    s=additional_legend, 
    transform=ax.transAxes,
    fontsize=10, 
    verticalalignment='baseline', 
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
)

# Função para atualizar cada quadro
def update(frame):
    line.set_data(comprimento_suavizado[:frame], 
    penetracao_suavizada[:frame])
    return line,

# Criação da animação
frames = len(comprimento_suavizado)
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Salvando o GIF
rc('animation', embed_limit=50)
ani.save("output/progressao_suavizada.gif", writer=PillowWriter(fps=10))
plt.close()

HTML(ani.to_jshtml())
