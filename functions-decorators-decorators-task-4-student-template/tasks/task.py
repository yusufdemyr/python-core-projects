# ### Functions. Decorators. Decorators. Task 4. 

# #### Decorators Factory

# Create a decorators factory (decorator itself). The factory accepts a function (lambda) as an input and returns a decorator 
# that will return the result of the function as the first argument, the result of the decorated function is passed. 
# The function which the factory accepts (in the example below it is a lambda) can take one positional parameter only.

# For example:
# ```python
# >>> @decorator_apply(lambda user_id: user_id + 1)
# >>> def return_user_id(num: int): 
#         return num
# >>> return_user_id(42) 
# >>> 43
# ```


def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return lambda_func(result)
        return wrapper
    return decorator

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
