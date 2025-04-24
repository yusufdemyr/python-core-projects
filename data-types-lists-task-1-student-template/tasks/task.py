# # Data Types. Lists. Task 1

# Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form.

# __Examples:__

# Input:
# ```python 
# ('red', 'white', 'black', 'red', 'green', 'black') 
# ```
# Output: 
# ```python 
# ['black', 'green', 'red', 'white']
# ```

from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    # TODO: Add your code here
    return sorted(set(str_list))

