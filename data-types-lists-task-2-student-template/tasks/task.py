# # Data Types. Lists. Task 2

# Update the __get_fizzbuzz_list__ function. The function has to generate and return a list with numbers from _1_ to _n_ 
# inclusive where the _n_ is passed as a parameter to the function. But if the number is divided by _3_ the function puts a _Fizz_ word into the list, 
# and if the number is divided by _5_ the function puts a _Buzz_ word into the list. 
# If the number is divided by both _3_ and _5_ the function puts _FizzBuzz_ into the list.

from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    fizzbuzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(i)
    return fizzbuzz_list

if __name__ == "__main__":
    # Test the function
    n = 15
    result = get_fizzbuzz_list(n)
    print(result)  # Expected output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']