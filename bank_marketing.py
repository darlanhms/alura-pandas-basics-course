import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
import pickle

data = pd.read_csv("./data/marketing_investimento.csv")

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
x_train, x_test, y_train, y_test = train_test_split(x_transformed, y_transformed, stratify=y, random_state=5)

# %%
dummy = DummyClassifier()
dummy.fit(x_train, y_train)

dummy.score(x_test, y_test)

# %%
tree_classifier = DecisionTreeClassifier(random_state=5, max_depth=3)
tree_classifier.fit(x_train, y_train)

tree_classifier.predict(x_test)

tree_classifier.score(x_train, y_train)

column_names = ['casado (a)',
                'divorciado (a)',
                'solteiro (a)',
                'fundamental',
                'medio',
                'superior',
                'inadimplencia',
                'fez_emprestimo',
                'idade',
                'saldo',
                'tempo_ult_contato',
                'numero_contatos']

plt.figure(figsize=(15, 6))
plot_tree(tree_classifier, filled=True, class_names=['nao', 'sim'], fontsize=7, feature_names=column_names);

# %%
scaler = MinMaxScaler()
x_train_normalized = scaler.fit_transform(x_train)
x_test_normalized = scaler.transform(x_test)

pd.DataFrame(x_train_normalized)

# %%
knn = KNeighborsClassifier()
knn.fit(x_train_normalized, y_train)

knn.score(x_test_normalized, y_test)

# %%
print(f'Dummy accuracy: {dummy.score(x_test, y_test)}')
print(f'Tree accuracy: {tree_classifier.score(x_test, y_test)}')
print(f'KNN accuracy: {knn.score(x_test_normalized, y_test)}')

# %%
with open("model_onehotenc.pkl", 'wb') as file:
    pickle.dump(one_hot, file)

# %%
with open("model_tree_classifier.pkl", 'wb') as tree_file:
    pickle.dump(tree_classifier, tree_file)

# %%
new_data = {
    'idade': [45],
    'estado_civil':['solteiro (a)'],
    'escolaridade':['superior'],
    'inadimplencia': ['nao'],
    'saldo': [23040],
    'fez_emprestimo': ['nao'],
    'tempo_ult_contato': [800],
    'numero_contatos': [4]
}

new_data = pd.DataFrame(new_data)

one_hot_model = pd.read_pickle("./model_onehotenc.pkl")
tree_classifier_model = pd.read_pickle("./model_tree_classifier.pkl")

# %%
normalized_new_data = one_hot_model.transform(new_data)

normalized_new_data
tree_classifier_model.predict(normalized_new_data)

# %%
