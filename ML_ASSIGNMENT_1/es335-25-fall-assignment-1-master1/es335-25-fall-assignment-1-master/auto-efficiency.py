import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *

np.random.seed(42)

# Reading the data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
data = pd.read_csv(url, sep=r'\s+', header=None,
                 names=["mpg", "cylinders", "displacement", "horsepower", "weight",
                        "acceleration", "model year", "origin", "car name"])

# Clean the above data by removing redundant columns and rows with junk values
# Compare the performance of your model with the decision tree module from scikit learn


data = data.replace("?", np.nan)
data = data.dropna()  
data = data.drop(columns=["car name"])  
data["horsepower"] = data["horsepower"].astype(float) 

X = data.drop(columns=["mpg"])
y = data["mpg"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tree = DecisionTree(criterion="mse", max_depth=5)
tree.fit(X_train, y_train)

y_hat = tree.predict(X_test)

print("Results from Custom Decision Tree:")
print("RMSE:", rmse(y_hat, y_test))
print("MAE:", mae(y_hat, y_test))

tree.plot()


from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

sklearn_tree = DecisionTreeRegressor(criterion="squared_error", max_depth=5, random_state=42)
sklearn_tree.fit(X_train, y_train)

y_hat_sklearn = sklearn_tree.predict(X_test)

print("\nResults from scikit-learn Decision Tree:")
print("RMSE:", root_mean_squared_error(y_test, y_hat_sklearn))  # RMSE
print("MAE:", mean_absolute_error(y_test, y_hat_sklearn))

import matplotlib.pyplot as plt
from sklearn import tree as sk_tree

plt.figure(figsize=(20, 10))
sk_tree.plot_tree(sklearn_tree, feature_names=X.columns, filled=True, rounded=True)
plt.show()