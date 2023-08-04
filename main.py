# Plotar seno e cosseno
import numpy as np
from matplotlib import pyplot as plt

def plotSinCos():
    # Definir o intervalo de amostragem
    t = np.arange(0.0, 2.0, 0.01)
    # Definir o sinal seno
    s = np.sin(2 * np.pi * t)
    # Definir o sinal cosseno
    c = np.cos(2 * np.pi * t)
    # Plotar o sinal seno
    plt.plot(t, s, 'r--')
    # Plotar o sinal cosseno
    plt.plot(t, c, 'b--')
    # Definir o título do gráfico
    plt.title('Seno e Cosseno')
    # Definir o label do eixo x
    plt.xlabel('Tempo (s)')
    # Definir o label do eixo y
    plt.ylabel('Amplitude')
    # Definir a legenda
    plt.legend(['Seno', 'Cosseno'])
    # Exibir o gráfico
    plt.show()
    
plotSinCos()