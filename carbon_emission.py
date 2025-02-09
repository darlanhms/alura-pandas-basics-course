import pandas as pd

gas_emissions = pd.read_excel("./data/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx", sheet_name="GEE Estados")

# %%
print(gas_emissions.head())
gas_emissions = gas_emissions[gas_emissions["Emissão / Remoção / Bunker"] == "Emissão"]

gas_emissions = gas_emissions.drop(columns="Emissão / Remoção / Bunker")

# %%
col_info = gas_emissions.loc[:, 'Nível 1 - Setor':'Produto'].columns.to_list()

emission_col_info = gas_emissions.loc[:, 1970:2021].columns.to_list()

# %%
yearly_emissions = gas_emissions.melt(id_vars = col_info, value_vars = emission_col_info, var_name = 'Ano', value_name = 'Emissão')

# %%
gas_emission_total = yearly_emissions.groupby('Gás').sum(numeric_only=True).sort_values("Emissão", ascending=False)

gas_emission_total.plot(kind="barh", figsize=(10, 6))

# %%
gas_emission_total.iloc[0:9]
print(f'A emissão de CO2 corresponde a {float((gas_emission_total.iloc[0:9].sum() / gas_emission_total.sum()).iloc[0]) * 100:.2f}% de emissão total de gases estufa no Brasil de 1970 até 2021')

# %%
gas_emission_by_sector = yearly_emissions.groupby(["Gás", "Nível 1 - Setor"])[["Emissão"]].sum()

max_values = gas_emission_by_sector.groupby(level=0).max().values

summarized_df = gas_emission_by_sector.groupby(level=0).idxmax()
summarized_df.insert(1, "Quantidade de emissão", max_values)

# %%
gas_emission_by_sector.swaplevel(0, 1).groupby(level=0).idxmax()

# %%
yearly_emissions.groupby("Ano")[["Emissão"]].mean().idxmax()

# %%
yearly_emission_mean = yearly_emissions.groupby(["Ano", "Gás"])[["Emissão"]].mean().reset_index()

yearly_emission_mean = yearly_emission_mean.pivot_table(index = "Ano", columns = "Gás", values = "Emissão")

yearly_emission_mean.plot(subplots=True, figsize=(10, 40));
# %%
