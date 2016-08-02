import numpy as np
with open('../data/train_data.csv', mode='r') as f:
    dataset = np.loadtxt(f, delimiter=',')

ids = dataset[1:,0]
features = dataset[1:, 1:5]
targets = dataset[1:, 5]

# normalizing data
from sklearn import preprocessing
n_features = preprocessing.normalize(features)

# feature selection

from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(n_features, targets)

print(model.feature_importances_)

# algorythm
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(n_features, targets)
print(model)

# predict
expected = targets
predicted = model.predict(n_features)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))