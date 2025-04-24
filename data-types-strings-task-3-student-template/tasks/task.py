# # Data Types. Strings. Task 3

# Implement a function that receives a string and replaces all `"` symbols
# with `'` and vice versa.

def replacer(s: str) -> str:
    """
    Add your code here
    """
    # Replace double quotes with single quotes and vice versa
    s = s.replace('"', 'temp').replace("'", '"').replace('temp', "'")
    # Return the modified string
    return s
