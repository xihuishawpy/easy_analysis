
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

class PcaMethod():
    def __init__(self,df):
        self.df = df

    def _standardize(self):
        return (self.df - self.df.mean()) / self.df.std()

    def main_component(self):
        normalized_df = self._standardize()
        pca = PCA()
        pca.fit(normalized_df)
        # 方差解释率
        variance_ratio = pca.explained_variance_ratio_
        # 特征根(特征根占比 = 方差解释率)
        roots = pca.explained_variance_
        # 载荷系数
        loadings = pca.components_

        # 获取方差累计解释率>0.9的主成分
        variance_ratio_cum = variance_ratio.cumsum()
        topk_index = np.argwhere( variance_ratio_cum > 0.9 ).min() + 1

        main_loading = loadings[:,:topk_index] # 主成分
        main_root = roots[:topk_index] # 对应特征根
        return main_loading, main_root

    def calculate_weights(self):
        main_loading, main_root = self.main_component()
        # 线性组合系数
        linear_coef = main_loading / np.sqrt(main_root)
        main_root_cum = (main_root * 10).sum()
        # 计算综合得分、权重
        score = np.dot(linear_coef, (main_root * 10)) / main_root_cum
        return score / sum(score)



if __name__ == '__main__':
    df = pd.read_csv('../test_data/test_pca_method.csv')

    pcam = PcaMethod(df)
    # 计算权重
    weights = pcam.calculate_weights()
    print(weights)

