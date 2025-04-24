# ### Functions. Decorators. Decorators. Task 3. 

# Create decorator `validate` which validates arguments in `set_pixel` function. All function parameters should be between 0(int) and 256(int) inclusive.

# In case if all parameters are valid, `set_pixel` function should return _"Pixel created!"_ message. Otherwise, it should return _"Function call is not valid!"_ message.

# Use `functools.wraps` where is it necessary.

# Don't forget about doc stings.

# __Examples__
# ```python
# >>> set_pixel(0, 127, 300)
# Function call is not valid!
# >>> set_pixel(0,127,250)
# Pixel created!
# ```
from functools import wraps

def validate(fn):
    '''
    Add corresponded arguments and implementation here. 
    '''
    @wraps(fn)
    def wrapper_function(*args,**kwargs):
      if all(0 <= arg <= 256 for arg in args):
          return fn(*args, **kwargs)
      else:
          return "Function call is not valid!"
    return wrapper_function

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  """Pixel created!"""
  return "Pixel created!"

