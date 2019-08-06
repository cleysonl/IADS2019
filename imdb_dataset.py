# !pip install shap
# !pip3 install lime


import numpy as np

from shap.datasets import imdb

from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import GlobalAveragePooling1D
from keras.layers import Dense

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from lime import lime_text
from lime.lime_text import LimeTextExplainer

data, labels = imdb()


