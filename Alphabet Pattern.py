# Write a Python program that takes two strings, a and b, where a is "ABCD" and b is "PQR". 
# The program should print a pattern of 4 lines where each line contains the characters from a replacing the last n characters with the first n characters from b, 
# where n ranges from 1 to the length of b. The pattern should look like this:

def print_pattern(a, b):
    # Validate inputs
    if not (isinstance(a, str) and isinstance(b, str)):
        raise ValueError("Both inputs must be strings.")
        
    # Calculate the length of the strings
    len_a, len_b = len(a), len(b)
    
    # Loop through each character in string b
    for i in range(len_b + 1):
        # Construct and print the pattern for each line
        print(a[:len_a - i] + b[:i])

# Define the strings
a = "ABCD"
b = "PQR"

# Call the function to print the pattern
print_pattern(a, b)
