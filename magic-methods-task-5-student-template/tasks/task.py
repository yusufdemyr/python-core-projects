# ## Magic methods. task 5
# ***
# Create a context manager `TempDir` (Use Context Manager protocol - methods `__enter__`, `__exit__`):
# 1. When entering the context, a new temporary directory is created with random, unique name.
#    Use `os.mkdir` to create the directory.
# 2. Until exiting this context the new created directory becomes current one and all actions are executed 
#    in scope of this new directory.
# 3. When exiting this context, the temporary directory is removed with all files in it.
#    Use `rmtree` from `shutil` to remove whole directory.
# 4. The new working directory becomes the same as before entering context.


import os
import shutil
import random

class TempDir:
    
    # TODO: please ad your code here
    def __enter__(self):
        self.random_name = str(random.random())
        self.working_dir = os.makedirs(f"./{self.random_name}")
        os.chdir(f"./{self.random_name}")
        return self.working_dir

    def __exit__(self,exc_type,exc_value,exc_traceback):
        os.chdir("..")
        shutil.rmtree(f"./{self.random_name}")
        return False
 