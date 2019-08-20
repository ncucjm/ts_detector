#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import statistical_features
import classification_features
import fitting_features
from time_series_detector.common import tsd_common


def extract_features(time_series, window):
    """
    Extracts three types of features from the time series.

    :param time_series: the time series to extract the feature of
    :type time_series: pandas.Series
    :param window: the length of window
    :type window: int
    :return: the value of features
    :return type: list with float
    """
    if not tsd_common.is_standard_time_series(time_series, window):
        # add your report of this error here...

        return []

    # spilt time_series
    split_time_series = tsd_common.split_time_series(time_series, window)
    # nomalize time_series
    normalized_split_time_series = tsd_common.normalize_time_series(split_time_series)
    max_min_normalized_time_series = tsd_common.normalize_time_series_by_max_min(split_time_series)
    s_features = statistical_features.get_statistical_features(normalized_split_time_series[4])
    f_features = fitting_features.get_fitting_features(normalized_split_time_series)
    c_features = classification_features.get_classification_features(max_min_normalized_time_series)
    # combine features with types
    features = s_features + f_features + c_features
    return features
