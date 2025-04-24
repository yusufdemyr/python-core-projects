# Inside README.md
# Data Types. Strings. Task 2

# Implement a function `get_longest_word(s: str) -> str` which returns the longest word in the given string. 
# The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on). 
# If there are multiple longest words in the string with the same length return the word that occurs first.

# __Example:__

# ```python
# >>> get_longest_word('Python is simple and effective!')
# 'effective!'
# ```

def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    # Split the string into words
    words = s.split()
    # Find the longest word
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    # Return the longest word
    return longest_word if longest_word else ''

    