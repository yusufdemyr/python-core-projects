# ## Magic methods. Task 4
# ***
# #### Description

# You have to implement class `Book` with attributes `price, author, name.`

# - `author` and `name` fields have to be immutable;
# - `price` field may be changes but has to be in `0 <= price <= 100` range.

# If user tries to change `author` or `name` fields after
# initialization or set price out of range, the `ValueError` should be raised.

# Implement descriptors `PriceControl` and `NameControl` to validate parameters.

# #### Example

#     >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
#     >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
#     Author='William Faulkner', Name='The Sound and the Fury', Price='12'
    
#     >>> b.price = 55
#     >>> b.price
#     55
#     >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
#     >>> b.price = 101  # => ValueError: Price must be between 0 and 100.
    
#     >>> b.author = "new author"  # => ValueError: Author can not be changed.
#     >>> b.name = "new name"      # => ValueError: Name can not be changed.


class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self,owner,value):
        self.private_value = f"_{value}"
    
    def __get__(self,obj,objtype=None):
        return getattr(obj,self.private_value)
    
    def __set__(self,obj,value):
        if value >= 0 and value <= 100:
            return setattr(obj,self.private_value,value)
        else:
            raise ValueError(f"{self.private_value[1:].capitalize()} must be between 0 and 100.")
            


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if hasattr(obj, self.private_name):
            raise ValueError(f"{self.private_name[1:].capitalize()} can not be changed.")
        setattr(obj, self.private_name, value)


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
    

