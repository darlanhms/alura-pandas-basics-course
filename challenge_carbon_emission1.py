import pandas as pd

gas_emissions = pd.read_excel("./1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx", sheet_name="GEE Estados")


gas_emissions.head()
#%%
# Encontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar as atividades econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.
gas_emissions["Nível 1 - Setor"].unique()
gas_emissions["Estado"].unique()

#%%
# Filtre o DataFrame somente com os dados dos Estados da região Sul do Brasil.
gas_emissions[gas_emissions["Estado"].isin(["SC", "RS", "PR"])]

#%%
# Filtre o DataFrame para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a "Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).
level_1_sector_selection = (gas_emissions["Nível 1 - Setor"] == "Mudança de Uso da Terra e Floresta") & (gas_emissions["Estado"] == "AM")
gas_emissions[level_1_sector_selection]

#%%
# Encontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.
agriculture_selection = (gas_emissions["Nível 1 - Setor"] == "Agropecuária") & (gas_emissions["Estado"] == "PA")
gas_emissions[agriculture_selection]
