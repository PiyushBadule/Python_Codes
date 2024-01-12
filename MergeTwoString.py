# Merge the two string
# Input:- a = "abc"
#         b = "def"
# Output:- adbecf
#
# Input:- a = "ab"
#         b = "zsd"
# Output:- azbsd
#
# Input:- a = "zbxnsjdns"
#         b = "idowdk"
# Output:- zibdxonwsdjkdns

def merge_strings(str1, str2):
    """
    Merges two strings by alternating characters from each.

    Args:
    str1 (str): The first string to be merged.
    str2 (str): The second string to be merged.

    Returns:
    str: A new string formed by alternating characters from str1 and str2. 
         If one string is longer, the remaining characters are appended at the end.
    """
    merged = []
    len_str1 = len(str1)
    len_str2 = len(str2)
    min_length = min(len_str1, len_str2)

    for i in range(min_length):
        merged.append(str1[i])
        merged.append(str2[i])

    # Append the remaining characters of the longer string
    if len_str1 > min_length:
        merged.append(str1[min_length:])
    elif len_str2 > min_length:
        merged.append(str2[min_length:])

    return ''.join(merged)

if __name__ == "__main__":
    str1 = 'zbxnsjdns'
    str2 = 'idowdk'
    result = merge_strings(str1, str2)
    print(result)
