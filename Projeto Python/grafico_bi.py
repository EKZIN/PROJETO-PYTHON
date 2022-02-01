import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("dados_brasil.xlsx")

plt.title("% de brasileiro infectados!")

plt.pie(planilha["TOTAL"], labels=planilha["PROPORÇÕES"], autopct="%1.2f%%")

plt.show()