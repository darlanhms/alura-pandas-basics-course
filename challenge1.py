import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv")

df.fillna(0, inplace=True)

df.drop(df.query("Nome == 'Alice' | Nome == 'Carlos'").index, inplace=True)

only_approved = df[df["Aprovado"] == True].copy()

only_approved["Notas"] = only_approved["Notas"].replace(7.0, 8.0)

only_approved.to_csv("approved_students.csv", index=False)