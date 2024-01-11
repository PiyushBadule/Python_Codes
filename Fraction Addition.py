# "Fraction Fusion"
# Introduction

# You are tasked with developing a function, add_fractions, which will aid in the arithmetic of fractions. Fractions, as you know, consist of two parts: a numerator and a denominator. Adding fractions is a fundamental task in mathematics and computing, but requires careful consideration of these components.

# Objective

# Your function will receive two fractions, each represented as a list of two integers [numerator, denominator]. The goal is to correctly add these fractions and return the result as a fraction in the same format.

# Requirements

# Input Validation: The function must handle cases where the denominators are zero, as this represents an undefined fraction.

# Fraction Addition:

# If the denominators of the two fractions are the same, simply add the numerators.
# If one of the fractions has a numerator of zero, return the other fraction as the sum.
# In all other cases, use the formula for adding fractions: 
# a/b + c/d = ad+bc/bd

# Result: The function should return the sum of the two fractions as a list [numerator, denominator].

# Examples

# Input: [2, 3], [1, 2]
# Output: [7, 6]

# Input: [0, 3], [0, 2]
# Output: [0, 0]

# Input: [1, 0], [3, 2]
# Output: [3, 2]

# Constraints

# The numerators and denominators are integers.
# Handle the case where the denominator is zero appropriately.


def add_fractions(fraction1, fraction2):
    """
    Add two fractions and return the result as a fraction.

    Args:
    fraction1 (list): A list of two integers representing the first fraction (numerator, denominator).
    fraction2 (list): A list of two integers representing the second fraction (numerator, denominator).

    Returns:
    list: A list of two integers representing the sum of the fractions.
    """
    # Extracting numerators and denominators
    num1, den1 = fraction1
    num2, den2 = fraction2

    # Handling zero denominator cases
    if den1 == 0 or den2 == 0:
        return [0, 0]

    # If denominators are the same
    if den1 == den2:
        return [num1 + num2, den1]

    # If either numerator is zero
    if num1 == 0:
        return fraction2
    if num2 == 0:
        return fraction1

    # General case: a/b + c/d = (ad + bc) / bd
    new_num = (num1 * den2) + (num2 * den1)
    new_den = den1 * den2
    return [new_num, new_den]

# Testing the function with different inputs
if __name__ == "__main__":
    print("Fraction addition [2, 3] + [1, 2]:", add_fractions([2, 3], [1, 2]))
    print("Fraction addition [0, 3] + [0, 2]:", add_fractions([0, 3], [0, 2]))
    print("Fraction addition [1, 0] + [3, 2]:", add_fractions([1, 0], [3, 2]))
