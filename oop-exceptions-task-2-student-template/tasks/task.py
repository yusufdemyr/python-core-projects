# ### OOP. Exceptions. Task 2
# ***
# #### Description

# Write a function `divide` which accepts a string that contains two integers, separated by **spaces** (integers can be separated by more than one space).
# You have to perform the division operation (`a / b`) and return the result (float) or an error message.

# The structure of the error message is the following: `Error code: {error message}`.

# #### Example

#     >>> divide("4 2")
#     2.0

#     >>> divide("4 0")
#     "Error code: division by zero"

#     >>> divide("* 1")
#     "Error code: invalid literal for int() with base 10: '*'"

from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    s = [word for word in str_with_ints.split(" ") if word.strip() != ""]
    try:
        result = int(s[0]) / int(s[1])
        return result
    except Exception as e:
        return f"Error code: {str(e)}"

