import pandas as pd
import numpy as np

def create_series_examples():
    """
    Demonstrates various ways to create and manipulate Pandas Series.
    Includes operations like creating Series, indexing, slicing, and basic arithmetic operations.
    """
    # Creating Series from a list
    list_s = [1, 2, -3, 6.2, 'data']
    series1 = pd.Series(list_s)
    print("Series from list:\n", series1)

    # Creating Series directly
    series2 = pd.Series([1, 2, 3, 4, 5])
    print("\nSeries directly created:\n", series2)

    # Creating Series with custom index
    series3 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print("\nSeries with custom index:\n", series3)

    # Creating Series with specified data type
    series4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype=float)
    print("\nSeries with data type:\n", series4)

    # Creating Series with name, data type, and index
    series5 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype=float, name='data values')
    print("\nNamed Series:\n", series5)

    # Creating Series from a scalar
    scalar_s = pd.Series(0.5)
    print("\nSeries from scalar:\n", scalar_s)

    # Series with scalar and multiple indices
    scalar_s = pd.Series(0.5, index=[1, 2, 3])
    print("\nSeries with scalar and multiple indices:\n", scalar_s)

    # Creating Series from a dictionary
    dict_s = pd.Series({'a': 1, 'b': 2})
    print("\nSeries from dictionary:\n", dict_s)

    # Operations on Series
    series6 = pd.Series([1, 2, 3, 4, 5])
    print("\nIndexing (First element):\n", series6[0])
    print("Max value:\n", max(series6))
    print("Min value:\n", min(series6))
    print("Slicing:\n", series6[0:3])
    print("Values greater than 3:\n", series6[series6 > 3])

    # Arithmetic operations
    series7 = pd.Series([1, 2, 3, 4, 5])
    print("\nAdding two Series:\n", series6 + series7)

    # Adding Series of different lengths
    series8 = pd.Series([1, 2, 3])
    print("\nAdding Series of different lengths:\n", series7 + series8)

    # Creating Series with NaN values
    s = pd.Series([1, 2, 3, 4, 5, 6, np.nan, 8, 9, 10])
    print("\nSeries with NaN values:\n", s)

    # Additional Operations
    # Mean, Median, Standard Deviation
    print("\nMean of series6:", series6.mean())
    print("Median of series6:", series6.median())
    print("Standard Deviation of series6:", series6.std())

def main():
    """
    Main function to demonstrate the creation and manipulation of Pandas Series.
    """
    create_series_examples()

if __name__ == "__main__":
    main()
