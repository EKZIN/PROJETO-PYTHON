import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("dados_crescente.xlsx")

num_infec = planilha["INFECTADOS"]

plt.title("A volta da crescente! - JANEIRO 2022")

plt.xlabel("DIAS ENTRE 24 A 28")
plt.ylabel("NÚMERO DE INFECTADOS")

plt.plot(num_infec, marker='o', linestyle='dashed', color='red')

plt.grid()

plt.show()