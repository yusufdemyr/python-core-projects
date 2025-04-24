# ## Magic methods. Task 6
# ***
# Create a context manager `Cd` which changes the current directory to pointed one.
# For example:
# ```python
# with Cd('/home')
# ```
# When entering the context you need to save the previous directory and when you exit you need to restore it.
# During context manager initialization check that the passed directory is a directory and exists.
# If the passed directory is not a directory or does not exist raise `ValueError`.
# Use the following functions from the `os` module: `getcwd`, `chdir`, `path.isdir`


import os


import os

class Cd:
    def __init__(self, path):
        self.new_path = os.path.abspath(path)
        self.old_path = None

    def __enter__(self):
        if not os.path.isdir(self.new_path):
            raise ValueError

        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        return True 

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.old_path:
            os.chdir(self.old_path)
        return False 
