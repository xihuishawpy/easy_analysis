# test entropy value method
import pandas as pd
df = pd.read_excel('./test_data/test_entropy_value_method.xlsx', index_col=0)

from weighting_evaluation import entropy_value_method as evm
evm = evm.EntropyValueMethod(df)

weights = evm.calculate_weights()
print(weights)
score = evm.calculate_scores()
print(score)

