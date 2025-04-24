# ## Functions. Decorators. Decorators. Task 2

# Write a decorator which logs information about calls of decorated function,
# values of its arguments, values of keyword arguments and execution time. Log
# should be written to a file.

# ### Example of using
# ``` python
# @log
# def foo(a, b, c):
#     ...

# foo(1, 2, c=3)
# ```

# ### log.txt
# ```
# ...
# foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
# ...
# ```
import time

def log(fn):
    """
    Add your code here or call it from here   
    """
    def wrapper_function(*args,**kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        f = open("log.txt","w")
        f.write(f"{fn.__name__}; args: {', '.join([f'{arg}={value}' for arg, value in zip(fn.__code__.co_varnames, args)])}; kwargs: {', '.join([f'{k}={v}' for k, v in kwargs.items()])}; execution time: {execution_time:.2f} sec.\n")
        f.close()
        return result

    return wrapper_function
