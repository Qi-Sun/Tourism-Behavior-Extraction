# python 3
# -*- coding:utf8 -*-
from BaseClasses.Weibo import Weibo
from typing import List, Dict
import datetime
import time
import numpy as np
import math

WholeDaySenconds = 24 * 60 * 60
PI = math.pi


class TemporalFeature(object):
    def __init__(self):
        self.feature_type = {'weekday': True, 'date': True, 'time': True, 'holiday': True}
        # TODO
        pass

    def config_feature(self, **kwargs):
        """
        配置需要计算的特征
        :param kwargs:
        :return:
        """
        for key in kwargs:
            if key in self.feature_type:
                self.feature_type[key] = kwargs[key]
        return

    def get_weibo_feature(self, weibo: Weibo):
        # TODO
        return []

    def _get_weekday_feature(self, ond_date: datetime):
        """
        获取周特征（一周中的某一天）
        :param ond_date:
        :return:
        """
        curWeekDay = ond_date.weekday()
        alpha = curWeekDay / 7 * 2 * PI
        return np.array([math.cos(alpha), math.sin(alpha)])

    def _get_date_feature(self, one_date: datetime):
        """
        获取日期特征（一年中的某一天）
        :param one_date:
        :return:
        """

        def __isLeapyear(year):
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                return True
            else:
                return False

        beginningOfYear = datetime.datetime(year=one_date.year, month=1, day=1)
        daynum2beginning = (one_date - beginningOfYear).days
        daynumWholeyear = 366 if __isLeapyear(one_date.year) else 365
        alpha = daynum2beginning / daynumWholeyear * 2 * PI
        return np.array([math.cos(alpha), math.sin(alpha)])

    def _get_time_feature(self, one_day_time: datetime):
        """
        获取时间特征（一天中的时刻，即24小时）
        :param one_day_time:
        :return:
        """
        seconds2zero = one_day_time.hour * 60 * 60 + one_day_time.minute * 60 + one_day_time.second
        alpha = seconds2zero / WholeDaySenconds * 2 * PI
        return np.array([math.cos(alpha), math.sin(alpha)])
