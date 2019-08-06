# !pip install lime
# !pip install shap

import numpy as np
import pandas as pd
import shap
from shap.datasets import adult
from collections import Counter

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

from IPython.display import Image  
import pydotplus

from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt

import lime 
import lime.lime_tabular


data, labels = adult(display=True)
labels = np.array([int(label) for label in labels])

column_names = list(data.columns)



# select categorical values of data
cat_cols = data.select_dtypes(['category']).columns





# code to visualise feature importance
figsize(12, 10)
plt.style.use('fivethirtyeight')

# Plot the 10 most important features in a horizontal bar chart
feature_results.loc[:9, :].plot(x = 'feature', y = 'importance', 
                                 edgecolor = 'k',
                                 kind='barh', color = 'blue');
plt.xlabel('Relative Importance', size = 20); plt.ylabel('')
plt.title('Feature Importance', size = 30);