import pandas as pd
import plotly.express as px
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier

data = pd.read_csv("./marketing_investimento.csv")

#%%
px.histogram(data, x="fez_emprestimo", text_auto=True, color="aderencia_investimento", barmode="group")

# %%
px.box(data, x="numero_contatos", color="aderencia_investimento")

# %%
x = data.drop("aderencia_investimento", axis=1)
y = data["aderencia_investimento"]

# %%
columns = x.columns

# %% Categorizing
one_hot = make_column_transformer((
        OneHotEncoder(drop="if_binary"),
        ["estado_civil", "escolaridade", "inadimplencia", "fez_emprestimo"]
    ),
    remainder="passthrough",
    sparse_threshold=0
)

x_transformed = one_hot.fit_transform(x)

feature_names = one_hot.get_feature_names_out(columns)

pd.DataFrame(x_transformed, columns=feature_names)

# %%
label_encoder = LabelEncoder()

y_transformed = label_encoder.fit_transform(y)

# %% Data separation
x_trained, x_test, y_trained, y_test = train_test_split(x_transformed, y_transformed, stratify=y, random_state=5)

# %%
dummy = DummyClassifier()
dummy.fit(x_trained, y_trained)

dummy.score(x_test, y_test)
# %%
