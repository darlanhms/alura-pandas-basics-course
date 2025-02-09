#%%
import pandas as pd
import json
import numpy as np
import seaborn as sns

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
sns.boxplot(x=no_null_df['cliente.tempo_servico'])

# %% Identifying outliers
Q1 = no_null_df['cliente.tempo_servico'].quantile(.25)
Q3 = no_null_df['cliente.tempo_servico'].quantile(.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
higher_limit = Q3 + 1.5 * IQR

outlier_filter = (no_null_df["cliente.tempo_servico"] < lower_limit) | (no_null_df["cliente.tempo_servico"] > higher_limit)

no_outliers_df = no_null_df.copy()

# %%
no_outliers_df.loc[outlier_filter, "cliente.tempo_servico"] = np.ceil(
    no_outliers_df.loc[outlier_filter, "conta.cobranca.Total"] /  no_outliers_df.loc[outlier_filter, "conta.cobranca.mensal"]
)

# %% Removing outliers
Q1 = no_outliers_df['cliente.tempo_servico'].quantile(.25)
Q3 = no_outliers_df['cliente.tempo_servico'].quantile(.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
higher_limit = Q3 + 1.5 * IQR

outlier_filter = (no_outliers_df["cliente.tempo_servico"] < lower_limit) | (no_outliers_df["cliente.tempo_servico"] > higher_limit)

# %%
no_outliers_df = no_outliers_df[~outlier_filter]

no_outliers_df.reset_index(drop=True, inplace=True)

# %% 
no_id_df = no_outliers_df.drop("id_cliente", axis=1).copy()

# %%
mapper = {
    'nao': 0,
    'sim': 1,
    'masculino': 0,
    'feminino': 1,
}

columns = ['telefone.servico_telefone', 'Churn', 'cliente.parceiro', 'cliente.dependentes', 'conta.faturamente_eletronico', 'cliente.genero']

# %%
no_id_df[columns] = no_id_df[columns].replace(mapper)

# %%
df_dummies = pd.get_dummies(no_id_df).copy()
