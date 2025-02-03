import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv")

data["Pontos_extras"] = data["Notas"] * 0.4
data["Notas_finais"] = data["Notas"] + data["Pontos_extras"]
data["Aprovado"] = data["Notas_finais"].apply(lambda x: True if x >= 6 else False)

approved_after_extras = data[(data["Aprovado"] == True) & (data["Notas"] < 6)]

approved_after_extras.head()
print(data)
