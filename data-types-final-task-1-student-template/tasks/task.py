# # Data Types. Final task 1

# Write a Python program to print all the unique values of all the dictionaries in a list.

# __Example__:
# ```
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    values = set()
    for d in lst:
        for v in d.values():
            values.add(v)
    return values

