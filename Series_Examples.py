import pandas as pd
import numpy as np

# Creating the Series with list
list_s = [1, 2, -3, 6.2, 'data']
series1 = pd.Series(list_s)
print(series1)
print(type(series1))

# Creating the Series with Direct giving list
series2 = pd.Series([1, 2, 3, 4, 5])
print(series2)

# Creating the Series and giving them Index
series3 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(series3)

# Creating the Series and mentioning DataType and Index
series4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype=float)
print(series4)

# Creating the Series and mentioning DataType, Index and name
series5 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype=float, name='data values')
print(series5)

# Creating Series with Scalar
scalar_s = pd.Series(0.5)
print(scalar_s)

# Creating the Series with Scalar and Multiple index
scalar_s = pd.Series(0.5, index=[1, 2, 3])
print(scalar_s)

# Creating the Series with Dictionary
dict_s = pd.Series({'a': 1, 'b': 2})
print(dict_s)

series6 = pd.Series([1, 2, 3, 4, 5])
# Access Series through Index
print("Index Value:-", series6[0])

# Max Value from Series
print("Max Value:-", max(series6))

# Min Value from Series
print("Min Value:-", min(series6))

# Slicing the Series
print(series6[0:3])

# Print Values from Series Greater than 3
print(series6[series6 > 3])

series7 = pd.Series([1, 2, 3, 4, 5])

# Adding Two Series
print(series6 + series7)

series8 = pd.Series([1, 2, 3])

# Adding Two Series with Different Length
print(series7 + series8)

# Creating Series with Some empty Values
s = pd.Series([1, 2, 3, 4, 5, 6, np.nan, 8, 9, 10])
print(s)
