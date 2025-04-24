# # Data Types. Dictionaries. Task 1.

# Write a Python program to count the frequency of each character in a string (ignore the case of letters).

# __Example:__

# Input: `'Oh, it is python'`

# Output: `{" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}`

from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    # string to lower case
    s = s.lower()
    # create an empty dictionary
    frequency_dict = {}
    # iterate through each character in the string
    for char in s:
        # if the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        # if the character is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[char] = 1
    # sort dict
    frequency_dict = dict(sorted(frequency_dict.items()))
    return frequency_dict
