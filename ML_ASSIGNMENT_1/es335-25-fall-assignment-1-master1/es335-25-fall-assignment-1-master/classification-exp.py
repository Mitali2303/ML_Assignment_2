import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from tree.base import DecisionTree

np.random.seed(42)

# Code given in the question
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=1,
    n_clusters_per_class=2, class_sep=0.5
)
X_df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
y_series = pd.Series(y, dtype='category')


# For plotting
plt.scatter(X[:, 0], X[:, 1], c=y)

# Write the code for Q2 a) and b) below. Show your results.


from sklearn.model_selection import train_test_split
from metrics import accuracy, precision, recall
from tree.base import DecisionTree

X_train, X_test, y_train, y_test = train_test_split(X_df, y_series, test_size=0.3, random_state=42)

tree = DecisionTree(criterion='information_gain') 
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

print("Accuracy: ", accuracy(y_pred, y_test))
for i in y_test.unique():
    print(f"Precision for class {i}: ", precision(y_pred, y_test, i))
    print(f"Recall for class {i}: ", recall(y_pred, y_test, i))


# 2b

class DecisionTreeWrapper(BaseEstimator, ClassifierMixin):
    def __init__(self, criterion='nformation_gain', max_depth=None):
        self.criterion = criterion
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = DecisionTree(criterion=self.criterion, max_depth=self.max_depth)
        self.tree.fit(X, y)
        
        self.classes_ = y.unique()
        return self

    def predict(self, X):
        return self.tree.predict(X)

param_grid = {'max_depth': list(range(1, 11))}

grid_search = GridSearchCV(
    DecisionTreeWrapper(criterion='information_gain'),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid_search.fit(X_df, y_series)

print("Best parameters (depth): ", grid_search.best_params_)
print("Best cross-validation score: ", grid_search.best_score_)

