import pandas as pd
import numpy as np


class EntropyValueMethod:
    def __init__(self, df):
        """
        df : input indicator
        """
        self.df = df

    def _standardize(self):
        """
        standardize indicator
        """
        return (self.df - self.df.min()) / (self.df.max() - self.df.min())

    def calculate_entropy(self):
        """
        Calculate entropy for each indicator in the dataframe
        """
        normalized_df = self._standardize()
        normalized_df = normalized_df / normalized_df.sum()

        entropy_df = normalized_df * np.log(normalized_df)
        entropy_df = entropy_df.fillna(0)
        self.entropy = - 1 / np.log(len(self.df)) * entropy_df.sum()
        self.entropy.name = '信息熵'
        return self.entropy

    def calculate_weights(self):
        """
        Calculate weights for each indicator in the dataframe
        """
        entropy = self.calculate_entropy()

        self.weights = (1 - entropy) / sum((1 - entropy))
        self.weights.name = '权重'
        return self.weights

    def calculate_scores(self):
        """
        Calculate scores for each sample in the dataframe
        """
        weights = self.calculate_weights()
        normalized_df = self._standardize()
        score = pd.Series(weights) * normalized_df
        score = score.sum(axis=1)
        self.score_df = pd.DataFrame({
            # 'ID': self.df.index,
            'Score': score
        })
        self.score_df.name ='加权得分'

        return self.score_df


if __name__ == '__main__':
    df = pd.read_excel('../test_data/test_entropy_value_method.xlsx',index_col=0)

    evm = EntropyValueMethod(df)
    # 计算权重
    weights = evm.calculate_weights()
    # # 输出加权得分
    score = evm.calculate_scores()
    # print(score)


