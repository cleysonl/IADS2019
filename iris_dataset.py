# !pip install lime
# !pip install graphviz
# !pip install pydotplus

from __future__ import print_function
np.random.seed(1)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

from IPython.display import Image  
import pydotplus

from collections import Counter
import pandas as pd
import numpy as np

import lime
import lime.lime_tabular


d = load_iris()
data = pd.DataFrame(data=d.data, columns=d.feature_names)
labels = [d.target_names[v] for v in d.target]

column_names = d.feature_names



# code to visualise a decision tree classifier
# clf is the classifier
# class_names are the classes that represent the labels
# feature_names are the names of the features
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_names,
                class_names=class_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('iris.png')
Image(graph.create_png())

