# ## Final tasks. Task 1

# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
# Implement singleton logic inside your custom class using a method to initialize class instance.

# Example:

# ```python
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True


class Sun:

    # TODO: please add your code here
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
