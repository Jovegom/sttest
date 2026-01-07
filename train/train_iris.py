from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle

# Cargar el dataset de Iris
iris = datasets.load_iris(as_frame=True)
X = iris['data']  # Características de las flores
y = iris['target']  # Etiquetas de las especies de flores

# Entrenar un modelo de regresión logística con los datos de Iris
log_reg = LogisticRegression().fit(X, y)

# Guardar el modelo entrenado en un archivo 'iris_model.pkl'
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(log_reg, f)