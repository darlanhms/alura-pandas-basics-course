# %%
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# %%
data = pd.read_csv("./data/emp_automovel.csv")

# %%
x = data.drop("inadimplente", axis=1)
y = data['inadimplente']

# %%
tree_classifier = DecisionTreeClassifier()
tree_classifier.fit(x, y)
tree_classifier.score(x, y)
print(f'Accuracy: {tree_classifier.score(x, y)}')

# %%
x, x_test, y, y_test = train_test_split(x, y, test_size=.15, stratify=y, random_state=5)

x_training, x_validation, y_training, y_validation = train_test_split(x, y, stratify=y, random_state=5)

# %%
tree_classifier = DecisionTreeClassifier(max_depth=10)
tree_classifier.fit(x_training, y_training)
print(f'Accuracy: {tree_classifier.score(x_training, y_training)}')
print(f'Accuracy validation: {tree_classifier.score(x_validation, y_validation)}')

# %%
y_preview = tree_classifier.predict(x_validation)
y_confusion_matrix = confusion_matrix(y_validation, y_preview)
print(y_confusion_matrix)

# %%
matrix_display = ConfusionMatrixDisplay(y_confusion_matrix, display_labels=["Adimplente", "Inadimplente"])
matrix_display.plot()

# %%
