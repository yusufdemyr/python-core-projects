# ## Functions. Decorators. Recursions. Task 1.
# Define a function `seq_sum(sequence)` which allows to count sum of elements. Elements of all nested sequences should be included.

# Example:
# ```python
# def seq_sum(sequence):
#     pass
  


# >>> print(seq_sum(sequence))
# 28
# ```
# }

from typing import List, Tuple, Union
from functools import reduce


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    return reduce(lambda x, y: x + (seq_sum(y) if isinstance(y, (list, tuple)) else y), sequence, 0)

# sequence = [1,2,3,[4,5, (6,7)]]