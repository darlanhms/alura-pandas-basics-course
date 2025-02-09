import pandas as pd
import json
import numpy as np

#%%
with open("./dataset-telecon.json") as dataset:
    raw_json = json.load(dataset)

normalized_data = pd.json_normalize(raw_json)

#%%
normalized_data[normalized_data["conta.cobranca.Total"] == " "][
    ["cliente.tempo_servico", "conta.contrato", "conta.cobranca.mensal", "conta.cobranca.Total"]
]

idx_tmp = normalized_data[normalized_data["conta.cobranca.Total"] == " "].index

normalized_data.loc[idx_tmp, "conta.cobranca.Total"] = normalized_data.loc[idx_tmp, "conta.cobranca.mensal"] * 24
normalized_data.loc[idx_tmp, "cliente.tempo_servico"] = 24

#%%
normalized_data["conta.cobranca.Total"] = normalized_data["conta.cobranca.Total"].astype(float)

# %%
for col in normalized_data.columns:
    print(f'Coluna: {col}')
    print(normalized_data[col].unique())
    print("-" * 30)

# %%
no_empty_data = normalized_data[normalized_data["Churn"] != ""].copy()

# %%
no_empty_data.reset_index(drop=True, inplace=True)

# %%
no_empty_data.drop_duplicates(inplace=True)

# %%
no_empty_data[no_empty_data['cliente.tempo_servico'].isna()]

no_empty_data["cliente.tempo_servico"].fillna(
    np.ceil(
        no_empty_data["conta.cobranca.Total"] /  no_empty_data["conta.cobranca.mensal"]
    ),
    inplace=True
)

# %%
no_empty_data[["conta.contrato", "conta.faturamente_eletronico", "conta.metodo_pagamento"]].isna().any(axis=1).sum()

no_null_df = no_empty_data.dropna(subset=["conta.contrato", "conta.faturamente_eletronico", "conta.metodo_pagamento"]).copy()
no_null_df.reset_index(drop=True, inplace=True)

# %%
