# 按分钟进行数据预处理

import pandas as pd
import numpy as np
import math

"""
dataframe数据结构时间戳处理


按秒采样时间戳ds和对应的y值，一天采样1440个点
        ds               y
2019-06-06 00:00:06    3652.0
2019-06-06 00:00:36    3615.0
2019-06-06 00:01:09    3615.0
2019-06-06 00:01:33    3610.0

属性：
    df : dataframe数据结构时间序列，时间序列按时间顺序将序
    start_time: 采样开始时间
    end_time: 采样结束时间
"""


class TimeStampUtil():

    def __init__(self, df, start_time="2019-6-6", end_time="2019-6-7"):

        self.start_time = start_time
        self.end_time = end_time

        self.df = df
        self.df["ds"] = pd.to_datetime(self.df["ds"])

        # 按天分割df

    def df_split(self):
        start_day = int(self.start_time.split("-")[-1])
        end_day = int(self.end_time.split("-")[-1])

        year = int(self.start_time.split("-")[0])
        month = int(self.end_time.split("-")[1])

        day_list = [day for day in range(start_day, end_day + 1)]
        date_list = [str(year) + "-" + str(month) + "-" + str(day) for day in day_list]

        df_list = []
        for index in range(len(date_list) - 1):
            start_point = date_list[index]
            end_point = date_list[index + 1]
            result = self.df[(self.df["ds"] > start_point) & (self.df["ds"] < end_point)]
            result = result.reset_index(drop=True)
            df_list.append(result)

        return df_list

    # 按天分割标准时间戳
    def time_stamp_split(self):

        time_stamp = pd.date_range(self.start_time, self.end_time, freq="MIN")
        num = math.floor(len(time_stamp) / 1440)

        index_start = 0
        index_end = 1440
        step = 1440

        time_stamp_list = []

        for index in range(num):
            if index == 0:
                temp_time_stamp = time_stamp[index_start:index_end]
                time_stamp_list.append(temp_time_stamp)
            else:
                index_start = index_start + step
                index_end = index_end + step
                temp_time_stamp = time_stamp[index_start:index_end]
                time_stamp_list.append(temp_time_stamp)

        return time_stamp_list

    # 按小时分割df
    def df_hour_split(self, df):

        hour_list = [str(hour) for hour in range(24)]
        for index in range(len(hour_list)):
            if len(hour_list[index]) < 2:
                hour_list[index] = '0' + hour_list[index]

        year = df["ds"][0].year
        month = df["ds"][0].month
        day = df["ds"][0].day

        hour_fragment = [str(year) + "-" + str(month) + "-" + str(day) + " " + hour for hour in hour_list]
        hour_fragment.append(str(year) + "-" + str(month) + "-" + str(day + 1) + " " + "00")
        df_hour_list = []

        for num in range(len(hour_fragment) - 1):
            start_hour = hour_fragment[num]
            end_hour = hour_fragment[num + 1]

            temp_df = df[(df["ds"] > start_hour) & (df["ds"] < end_hour)]

            temp_df = temp_df.iloc[range(0, len(temp_df), 2)]
            temp_df = temp_df.reset_index(drop=True)

            df_hour_list.append(temp_df)

        return df_hour_list

    # 按小时分割时间戳
    def time_stamp_hour_split(self, time_pattern):

        step = 60
        time_pattern = time_pattern[0:1440]
        hour_split_list = []

        for num in range(24):

            if num == 0:
                index_start = 0
                index_end = step
            else:
                index_start = index_start + step
                index_end = index_end + step

            temp_list = time_pattern[index_start:index_end]
            hour_split_list.append(temp_list)

        return hour_split_list

    def sample(self):

        df_list = self.df_split()
        time_stamp_list = self.time_stamp_split()
        temp_data_list = []
        temp_data = pd.DataFrame(columns=("ds", "y"))

        for num in range(len(df_list)):
            # 按小时分割此df
            temp_df = df_list[num]
            df_hour_list = self.df_hour_split(temp_df)

            time_pattern = time_stamp_list[num]

            # 按小时分割time_pattern
            time_stamp_hour_list = self.time_stamp_hour_split(time_pattern)

            for num1 in range(len(time_stamp_hour_list)):

                df_hour = df_hour_list[num1]
                time_stamp_hour = time_stamp_hour_list[num1]

                time_stamp_index = 0
                data_index = 0

                while time_stamp_index < len(time_stamp_hour):

                    if data_index == len(df_hour):
                        break

                    df_minute = df_hour["ds"][data_index].minute

                    time_stamp_minute = time_stamp_hour[time_stamp_index].minute

                    if df_minute == time_stamp_minute:

                        temp_data.loc[time_stamp_index] = {"ds": time_stamp_hour[time_stamp_index],
                                                           "y": df_hour["y"][data_index]}
                        time_stamp_index += 1
                        data_index += 1

                    elif df_minute < time_stamp_minute:

                        data_index += 1

                    elif df_minute > time_stamp_minute:

                        temp_data.loc[time_stamp_index] = {"ds": time_stamp_hour[time_stamp_index], "y": None}
                        time_stamp_index += 1

                while time_stamp_index < len(time_stamp_hour):
                    temp_data.loc[time_stamp_index] = {"ds": time_stamp_hour[time_stamp_index], "y": None}
                    time_stamp_index += 1

                temp_data_list.append(temp_data)
                temp_data = pd.DataFrame(columns=("ds", "y"))

        sample_result = pd.concat(temp_data_list)
        sample_result = sample_result.reset_index(drop=True)

        return sample_result

def data_process_1(df, path):
    source_data = pd.read_csv(path,header=None,sep="")