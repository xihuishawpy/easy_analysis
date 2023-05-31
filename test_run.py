
from weighting_evaluation import entropy_value_method as evm
import pandas as pd

df = pd.read_excel('./test_data/test_entropy_value_method.xlsx', index_col=0)
evm = evm.EntropyValueMethod(df)
weights = evm.calculate_weights()
score = evm.calculate_scores()

print(weights)
print(score)

