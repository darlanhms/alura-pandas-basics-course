import pandas as pd
import plotly.express as px

data = pd.read_csv("./marketing_investimento.csv")


#%%
px.histogram(data, x="fez_emprestimo", text_auto=True, color="aderencia_investimento", barmode="group")

# %%
