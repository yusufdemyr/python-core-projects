# ### Functions. Decorators. Functions arguments. Task 0. 
# ***

# Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.

# **Example:**
# ```python
# >>> generate_squares(5)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```

from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Add your code here or call it from here   
    """

    return {i: i**2 for i in range(1, num + 1)}

