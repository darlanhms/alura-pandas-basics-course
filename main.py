import pandas as pd

def plot_data_frame(data: pd.DataFrame):
    # get only value column, sort it and turn into a DataFrame
    df_price_type = data.groupby('Tipo')[["Valor"]].mean(numeric_only=True).sort_values("Valor")

    # plot bar chart
    df_price_type.plot(kind='barh', figsize=(14, 10))
    

#%%
data = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv", sep=";")

plot_data_frame(data)
#%%
# Filter only residencial real states
commercial_real_state_types = ['Conjunto Comercial/Sala', 
                                'Prédio Inteiro', 'Loja/Salão', 
                                'Galpão/Depósito/Armazém', 
                                'Casa Comercial', 'Terreno Padrão',
                                'Loja Shopping/ Ct Comercial',
                                'Box/Garagem', 'Chácara',
                                'Loteamento/Condomínio', 'Sítio',
                                'Pousada/Chalé', 'Hotel', 'Indústria']

df = data.query("@commercial_real_state_types != Tipo")

plot_data_frame(df)

# %%
# Understand what type os more present on the database
percent_type_df =df.Tipo.value_counts(normalize=True).to_frame().sort_values("Tipo")
percent_type_df.plot(kind="bar", figsize=(14, 10), xlabel="Tipos", ylabel="Percentual")

# %%
df = df.query("Tipo == 'Apartamento'")


# %%
