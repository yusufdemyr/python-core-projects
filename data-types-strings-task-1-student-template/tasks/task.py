# Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result. 
# __For example:__
# ```python
# >>> a_b = '1/3'
# >>> c_b = '5/3'
# >>> get_fractions(a_b, c_b)
# '1/3 + 5/3 = 6/3'
# ```

def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    # Split the fractions into numerator and denominator
    a, b = map(int, a_b.split('/'))
    c, d = map(int, c_b.split('/'))
    # Check if the denominators are the same
    if b == d:
        # Calculate the sum of the fractions
        numerator_sum = a + c
        # Create the result string
        result = f"{a}/{b} + {c}/{d} = {numerator_sum}/{b}"
        return result
    else:
        return ''
    

