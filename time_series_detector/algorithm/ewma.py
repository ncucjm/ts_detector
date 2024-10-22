#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np


class Ewma(object):
    """
    In statistical quality control, the EWMA chart (or exponentially weighted moving average chart)
    is a type of control chart used to monitor either variables or attributes-type data using the monitored business
    or industrial process's entire history of output. While other control charts treat rational subgroups of samples
    individually, the EWMA chart tracks the exponentially-weighted moving average of all prior sample means.

    WIKIPEDIA: https://en.wikipedia.org/wiki/EWMA_chart
    """

    def __init__(self, alpha=0.3, coefficient=3):
        """
        :param alpha: Discount rate of ewma, usually in (0.2, 0.3).
        :param coefficient: Coefficient is the width of the control limits, usually in (2.7, 3.0).
        """
        self.alpha = alpha
        self.coefficient = coefficient

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.

        :param X: the time series to detect of
        :param type X: pandas.Series
        :return: 1 denotes normal, 0 denotes abnormal
        """
        s = [X[0]]
        for i in range(1, len(X)):
            temp = self.alpha * X[i] + (1 - self.alpha) * s[-1]
            s.append(temp)
        s_avg = np.mean(s)
        sigma = np.sqrt(np.var(X))
        ucl = s_avg + self.coefficient * sigma * np.sqrt(self.alpha / (2 - self.alpha))
        lcl = s_avg - self.coefficient * sigma * np.sqrt(self.alpha / (2 - self.alpha))
        if s[-1] > ucl or s[-1] < lcl:
            return 0
        return 1
