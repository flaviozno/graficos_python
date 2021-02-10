import pandas as pd

tabela_clientes = pd.read_csv(r"/content/drive/MyDrive/Colab Notebooks/ClientesBanco.csv", encoding="latin1") #latin evita o erro utf-8
tabela_clientes = tabela_clientes.drop("CLIENTNUM", axis=1) #remove uma coluna, se colocar 0 exclui linha
display(tabela_clientes)

tabela_clientes = tabela_clientes.dropna() #remove linhas vazias
display(tabela_clientes.info())
display(tabela_clientes.describe())

display(tabela_clientes["Categoria"].value_counts(normalize=True)) #normalize mostra percentualmente

import plotly.express as px

for coluna in tabela_clientes:
  fig = px.histogram(tabela_clientes, x=coluna, color="Categoria")
  fig.show()