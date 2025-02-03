import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv', sep=';')

data["Valor_por_mes"] = data["Valor"] + data["Condominio"]
data["Valor_por_ano"] = (data["Valor"] + data["Condominio"]) * 12 + data["IPTU"]

data["Descricao"] = data["Tipo"] + ' em ' + data["Bairro"] + ' com ' + \
                    data["Quartos"].astype(str) + ' quarto(s)' + \
                    " e " + data["Vagas"].astype(str) + " vaga(s) de garagem."

data["Possui_suite"] = data["Suites"].apply(lambda x: "Sim" if x > 0 else "Não")

data.to_csv("complete_data.csv", index=False, sep=";")