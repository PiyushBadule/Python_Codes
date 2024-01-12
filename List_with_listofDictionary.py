# Convert list of dict to dict [[{},{}],[{},{}]]
# input: [[{'name': "piyush", "rank": 10}, {"name": "rahul", "rank": 20}],
#      [{"rank": 10, "class": 1}, {"rank": 20, "class": 3}]]
# output: [{'name': 'piyush', 'rank': 10, 'class': 1}, {'name': 'rahul', 'rank': 20, 'class': 3}]
def merge_dicts_based_on_rank(data):
    """
    Merges dictionaries from two sublists of a list based on a shared 'rank' key.
    Each dictionary in the first sublist is updated with the corresponding dictionary
    from the second sublist that has the same 'rank' value.

    Args:
    data (list of list of dict): A list containing two sublists of dictionaries.
        The first sublist is the primary list whose elements will be updated.
        The second sublist contains dictionaries that will be used for updating.

    Returns:
    list of dict: A list containing the updated dictionaries from the first sublist.
    """
    if len(data) != 2 or not all(isinstance(sublist, list) for sublist in data):
        raise ValueError("Input must be a list containing two sublists")

    merged_dicts = []
    primary_list = data[0]
    secondary_list = data[1]

    for primary_dict in primary_list:
        for secondary_dict in secondary_list:
            if primary_dict.get("rank") == secondary_dict.get("rank"):
                primary_dict.update(secondary_dict)
                break
        merged_dicts.append(primary_dict)

    return merged_dicts

if __name__ == "__main__":
    input_data = [[{'name': "piyush", "rank": 10}, {"name": "rahul", "rank": 20}],
                  [{"rank": 10, "class": 1}, {"rank": 20, "class": 3}]]
    result = merge_dicts_based_on_rank(input_data)
    print(result)
