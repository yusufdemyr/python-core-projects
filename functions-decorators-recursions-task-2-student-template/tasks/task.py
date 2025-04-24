# ## Functions. Decorators. Recursions. Task 2.
# Define a function `linear_seq(sequence)` which converts a passed sequence to a sequence without nested sequences.

# Example:
# ```python
# def linear_seq(sequence):
#     pass
  
# sequence = [1,2,3,[4,5, (6,7)]]

# >>> print(linear_seq(sequence))
# [1,2,3,4,5,6,7]
# ```


from typing import Any, List
from functools import reduce
def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    return reduce(lambda x,y: x + (linear_seq(y) if isinstance(y,(list,tuple)) else [y])   ,sequence,[])

