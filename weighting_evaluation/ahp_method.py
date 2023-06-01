
# AHP层次分析法
# https://mp.weixin.qq.com/s?__biz=MzI4OTUxMjMxNA==&mid=2247483738&idx=1&sn=9507e8657b2a96485264c7817167397e&chksm=ec2f4f4fdb58c6595d04b965c669db3cfe5c16fbf192079a93b08a94a37175cf87d8809af4a2&token=1287337162&lang=zh_CN#rd

import pandas as pd
import numpy as np

class AhpMethod():

    def __init__(self,df, method='arithmetic_mean'):
        "df : Judgment Matrix"
        self.df = df
        self.method = method

    def calculate_matrix(self):
        "arithmetic_mean"
        df_ratio = self.df / self.df.sum()
        weights = df_ratio.sum(axis=1)
        return weights


    def calculate_matrix2(self):
        "geometric_mean"
        weights = pow(self.df.prod(axis=1),1/4)
        return weights

    def choose_method(self):
        if self.method == 'arithmetic_mean':
            return self.calculate_matrix()
        elif self.method == 'geometric_mean':
            return self.calculate_matrix2()
        else:
            raise ValueError("Invalid method value: {}".format(self.method))
    






