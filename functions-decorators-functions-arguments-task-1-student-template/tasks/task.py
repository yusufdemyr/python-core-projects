# ### Functions. Decorators. Functions arguments. Task 1. 
# ***

# We have a list of dictionaries:
# ```python
# friends = [
#     {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
#     {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
# ]
# ```
# Create functions `query`, `select`, `field_filter` to work with lists similar to 
# `friends`.
# Stubs for these functions are already created.

# Example:
# ```python
# >>> result = query(
#     friends,
#     select('name', 'gender', 'sport'),
#     field_filter('sport', *('Basketball', 'volleyball')),
#     field_filter('gender', *('male',)),
# )
# >>> result
# [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]
# ```
# These functions have to provide with possibility to select necessary columns
# and make filtering by these columns

# Do not forget the documentation for each function!

from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    filtered_data = []
    for row in data:
        if all(filter_func([row]) for filter_func in filters):
            filtered_data.append(row)
    return selector(filtered_data)




def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    return lambda data: [
        {column: row[column] for column in columns if column in row}
        for row in data
    ]



def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    return lambda data: [
        row for row in data if row.get(column) in values
    ]


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    print(value)
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

