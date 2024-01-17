import sys

def smallest_sum_subarray(arr):
    """
    Find the smallest sum of a contiguous subarray in the given array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The smallest sum of a contiguous subarray.
    """
    temp_sum = sys.maxsize
    min_sum = sys.maxsize

    for num in arr:
        if temp_sum > 0:
            temp_sum = num
        else:
            temp_sum += num

        min_sum = min(min_sum, temp_sum)

    return min_sum

def main():
    """
    Main function to demonstrate finding the smallest sum of a contiguous subarray.
    """
    arr = [3, -4, 2, -3, -1, 7, -5]
    print("Smallest sum: ", smallest_sum_subarray(arr))

if __name__ == "__main__":
    main()
