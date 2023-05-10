# A naives bayes classifier

from sklearn.naive_bayes import GaussianNB
import numpy as np


def model(train_x, train_y):
    clf = GaussianNB()
    clf.fit(train_x, train_y)
    return clf
