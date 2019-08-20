#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from time_series_detector.common.tsd_common import *


class PolynomialInterpolation(object):
    """
    In statistics, polynomial regression is a form of regression analysis in which the relationship
    between the independent variable x and the dependent variable y is modelled as an nth degree polynomial in x.

    WIKIPEDIA: https://en.wikipedia.org/wiki/Polynomial_regression
    """

    def __init__(self, threshold=0.15, degree=4):
        """
       :param threshold: The critical point of normal.
       :param degree: Depth of iteration.
        """
        self.degree = degree
        self.threshold = threshold

    def predict(self, X, window=DEFAULT_WINDOW):
        """
        Predict if a particular sample is an outlier or not.

        :param X: the time series to detect of
        :param type X: pandas.Series
        :param window: the length of window
        :param type window: int
        :return: 1 denotes normal, 0 denotes abnormal
        """
        x_train = list(range(0, 2 * window + 1)) + list(range(0, 2 * window + 1)) + list(range(0, window + 1))
        x_train = np.array(x_train)
        x_train = x_train[:, np.newaxis]
        avg_value = np.mean(X[-(window + 1):])
        if avg_value > 1:
            y_train = X / avg_value
        else:
            y_train = X
        model = make_pipeline(PolynomialFeatures(self.degree), Ridge())
        model.fit(x_train, y_train)
        if abs(y_train[-1] - model.predict(np.array(x_train[-1]).reshape(1, -1))) > self.threshold:
            return 0
        return 1
