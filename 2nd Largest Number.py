# Question: Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
# Find the second Largest number from an given integer array
# Input:5
# 2 3 6 6 5
def find_runner_up_score(scores):
    """
    Finds the runner-up score (second highest unique score) from a list of scores.

    Parameters:
    scores (list): A list of integers representing the scores.

    Returns:
    int: The runner-up score.
    """

    # Remove duplicates and sort the list in ascending order
    unique_scores = sorted(set(scores))

    # The runner-up is the second last item in the sorted unique scores list
    runner_up = unique_scores[-2]

    return runner_up


def main():
    """
    Main function to take input and print the runner-up score.
    """

    # Input for the number of scores
    try:
        n = int(input("Enter the number of scores: "))
    except ValueError:
        print("Please enter a valid integer for the number of scores.")
        return

    # Input for scores, space-separated
    try:
        scores = list(map(int, input("Enter the scores separated by space: ").split()))
        if len(scores) != n:
            raise ValueError("The number of scores entered does not match the expected count.")
    except ValueError as e:
        print(f"Invalid input for scores. {e}")
        return

    # Find and display the runner-up score
    try:
        runner_up = find_runner_up_score(scores)
        print(f'Runner-up score is {runner_up}')
    except IndexError:
        print("Couldn't find the runner-up score. Please ensure there are at least two unique scores.")


# Standard boilerplate to call the main() function
if __name__ == '__main__':
    main()
