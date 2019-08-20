#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np


class Statistic(object):
    """
    In statistics, the 68-95-99.7 rule is a shorthand used to remember the percentage of values
    that lie within a band around the mean in a normal distribution with a width of two, four and
    six standard deviations, respectively; more accurately, 68.27%, 95.45% and 99.73% of the values
    lie within one, two and three standard deviations of the mean, respectively.

    WIKIPEDIA: https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    """

    def __init__(self, index=3):
        """
        :param index: multiple of standard deviation
        :param type: int or float
        """
        self.index = index

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.

        :param X: the time series to detect of
        :param type X: pandas.Series
        :return: 1 denotes normal, 0 denotes abnormal
        """
        if abs(X[-1] - np.mean(X[:-1])) > self.index * np.std(X[:-1]):
            return 0
        return 1
