import os
import numpy as np
from pandas import DataFrame, Categorical
from sklearn.datasets import make_classification
np.random.seed(47404)

'''Script used to generate random.csv data for Module 3'''

## Define parameters.
n_samples = 200       # The number of samples.
n_features = 10       # The total number of features (before any custom edits).
n_informative = 5     # The number of informative features.
n_redundant = 1       # The number of redundant features.
n_classes = 4         # The number of classes (or labels) of the classification problem.
flip_y = 0.10         # The fraction of samples whose class are randomly exchanged.

## Make shift/scale offsets.
shift = np.random.normal(0,5,n_features)
scale = (0.5 - np.random.beta(0.5,0.5,n_features)) * 4

## Initial simulation of data.
X, y = make_classification(n_samples=n_samples, n_features=n_features, 
                           n_informative=n_informative, n_redundant=n_redundant, 
                           n_classes=n_classes, n_clusters_per_class=1, flip_y=flip_y, 
                           shift=shift, scale=scale, random_state=0)

## Add further noise to X.
X += np.array([ np.random.normal(0, sd * 0.1, n_samples) for sd in X.std(axis=0) ]).T

## Stack data together.
data = np.c_[y,X]

## Convert to DataFrame.
data = DataFrame(data, columns=['y']+['x%0.2d' %n for n in np.arange(data.shape[-1] - 1) + 1])

## Rename y.
categories = ['yankee', 'foxtrot', 'hotel', 'tango']
data.y = Categorical(data.y, ordered=True).rename_categories(categories)

## Save.
data.to_csv('random.csv', index=False)