# # Data Types. Tuples. Task 1

# Implement a function `get_tuple(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.

# __Example:__
# ```python
# >>> get_tuple(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```


from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    # First string then list thn tuple
    str_num = str(num)  # Convert the integer to a string
    digits_list = [int(digit) for digit in str_num]  # Create a list of digits as integers
    return tuple(digits_list)

