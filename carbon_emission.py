import pandas as pd

gas_emissions = pd.read_excel("./1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx", sheet_name="GEE Estados")

# %%
print(gas_emissions.head())
gas_emissions = gas_emissions[gas_emissions["Emissão / Remoção / Bunker"] == "Emissão"]

gas_emissions = gas_emissions.drop(columns="Emissão / Remoção / Bunker")

gas_emissions
# %%
