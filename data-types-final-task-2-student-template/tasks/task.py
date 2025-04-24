# # Data Types. Final task 2

# Write a program which makes a pretty print of a part of the multiplication table.

# __Example__:
# ```
# Input:
# row_start = 2
# row_end = 4
# column_start = 3
# column_end = 7

# Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
# that is equal to the following multiplication table:

#     3   4   5   6   7   
# 2   6   8   10  12  14  
# 3   9   12  15  18  21  
# 4   12  16  20  24  28

from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    # Create an empty list to store the multiplication table
    multiplication_table = []

    # Iterate through the specified rows
    for i in range(row_start, row_end + 1):
        # Create a new row for the current value of i
        row = []
        # Iterate through the specified columns
        for j in range(column_start, column_end + 1):
            # Calculate the product and append it to the row
            row.append(i * j)
        # Append the completed row to the multiplication table
        multiplication_table.append(row)

    return multiplication_table
