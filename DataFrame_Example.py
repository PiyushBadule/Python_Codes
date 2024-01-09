import pandas as pd
import numpy as np

def create_dataframes():
    """
    Creates various types of Pandas DataFrames and prints them.
    This function demonstrates the creation of DataFrames using:
    - Empty DataFrame
    - Date range
    - List
    - List of lists
    - Dictionary
    - List of dictionaries
    - Pandas Series
    - NumPy array
    """

    # Creating an Empty DataFrame
    empty_df = pd.DataFrame()
    print("Empty DataFrame:")
    print(empty_df)

    # DataFrame Using DateRange
    date_range_df = pd.DataFrame(pd.date_range('20220107', periods=10))
    print("\nDataFrame with Date Range:")
    print(date_range_df)

    # DataFrame Using List
    list_df = pd.DataFrame(['a', 'b', 'c'])
    print("\nDataFrame from a List:")
    print(list_df)

    # DataFrame Using List of List
    list_of_list_df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nDataFrame from a List of Lists:")
    print(list_of_list_df)

    # DataFrame Using Dictionary
    dict_df = pd.DataFrame({'ID': [1, 2, 3, 4, 5]})
    print("\nDataFrame from a Dictionary:")
    print(dict_df)

    # DataFrame Using Dictionary with multiple columns
    multi_col_dict_df = pd.DataFrame({'ID': [101, 102, 103, 104], 'Name': ['A', 'B', 'C', 'D']})
    print("\nDataFrame from a Dictionary with Multiple Columns:")
    print(multi_col_dict_df)

    # DataFrame Using List of Dictionary
    list_of_dict_df = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
    print("\nDataFrame from a List of Dictionaries:")
    print(list_of_dict_df)
    list_of_dict_df2 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}])
    print("\nDataFrame from a List of Dictionaries with different keys:")
    print(list_of_dict_df2)

    # DataFrame Using Series
    series_df = pd.DataFrame({'ID': pd.Series([1, 2, 3]), 'Name': pd.Series(['A', 'B', 'C'])})
    print("\nDataFrame from Pandas Series:")
    print(series_df)

    # DataFrame Using Numpy Array
    numpy_df = pd.DataFrame({'A': np.array([5] * 10, dtype='int32')})
    print("\nDataFrame from a NumPy Array:")
    print(numpy_df)

def main():
    create_dataframes()

if __name__ == "__main__":
    main()
