# Sort it first on the basis of age then on the basis of salary.
import pandas as pd

def sort_dataframe(dataframe, sort_keys):
    """
    Sorts a DataFrame first by age, then by salary.

    Args:
    dataframe (pd.DataFrame): The DataFrame to be sorted.
    sort_keys (list): List of column names on which the DataFrame will be sorted.

    Returns:
    pd.DataFrame: The sorted DataFrame.
    """
    try:
        sorted_df = dataframe.sort_values(by=sort_keys)
        return sorted_df
    except KeyError as e:
        print(f"KeyError: {e} - Please check the column names.")
        return dataframe
    except Exception as e:
        print(f"An error occurred: {e}")
        return dataframe

def main():
    """
    Main function to demonstrate sorting a DataFrame by multiple columns.
    """
    data = [
        {'name': 'a', 'salary': 20000, 'age': 25},
        {'name': 'b', 'salary': 25000, 'age': 23},
        {'name': 'c', 'salary': 34000, 'age': 25},
        {'name': 'd', 'salary': 13000, 'age': 30}
    ]

    df = pd.DataFrame(data)

    # Sorting by 'age' and then by 'salary'
    sorted_df = sort_dataframe(df, ['age', 'salary'])
    print("DataFrame sorted by age and then salary:\n", sorted_df)

if __name__ == "__main__":
    main()
