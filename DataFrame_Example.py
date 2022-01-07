import pandas as pd
import numpy as np

# Creating Empty DataFrame
emt_df = pd.DataFrame()
print(emt_df)

# DataFrame Using DateRange
d = pd.date_range('20220107', periods=10)
df1 = pd.DataFrame(d)
print(df1)

# DataFrame Using List
df2 = pd.DataFrame(['a', 'b', 'c'])
print(df2)

# DatFrame Using List of List
df3 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df3)

# DataFrame Using Dictionary
df4 = pd.DataFrame({'ID': [1, 2, 3, 4, 5]})
print(df4)

# DataFrame Using Dictionary
df5 = pd.DataFrame({'ID': [101, 102, 103, 104], 'Name':['A', 'B', 'C', 'D']})
print(df5)

# DataFrame Using List of Dictionary
df6 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
print(df6)
df7 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}])
print(df7)

# DataFrame Using Series
df8 = pd.DataFrame({'ID': pd.Series([1, 2, 3]),
                    'Name': pd.Series(['A', 'B', 'C'])})
print(df8)

# DataFrame Using Numpy Array
df9 = pd.DataFrame({'A': np.array([5] * 10, dtype='int32')})
print(df9)