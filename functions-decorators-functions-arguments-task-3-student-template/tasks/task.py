# ### Functions. Decorators. Functions arguments. Task 3. 
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values should be summarized in case of identical keys

# ```python
# def combine_dicts(*args):
#     ...

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2))
# >>> {'a': 300, 'b': 200, 'c': 300}

# print(combine_dicts(dict_1, dict_2, dict_3))
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}

from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    """
    Combine multiple dictionaries into one, summing values for identical keys.
    
    :param args: Dictionaries to combine
    :return: Combined dictionary with summed values for identical keys
    """
    my_dict = {}
    for i, d in enumerate(args):
        for key, value in d.items():
            if key in my_dict.keys():
                my_dict[key] += value
            else:
                my_dict[key] = value
    
    return my_dict
