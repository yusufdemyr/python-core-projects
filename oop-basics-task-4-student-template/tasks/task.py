# ## OOP Basics. Task 4

# Implement a custom dictionary that will memorize the 5 latest changed keys.
# Using method "get_history" return these keys.

# Example:
# ```python
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]
# ```

# *After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque*

from collections import deque
class HistoryDict:
    
    def __init__(self,item):
        self._data = dict(item or {})
        self._history = deque(maxlen=5)

    def set_value(self,key,value):
        if self._data.get(key) != value:
            self._data[key] = value
            self._history.append(key)

    def get_history(self):
        return list(self._history)       

