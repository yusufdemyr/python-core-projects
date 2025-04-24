# # Data Types. Strings. Task 4

# Write a function that checks whether a string is a palindrome or not. The usage of
# any reversing functions is prohibited.
 
# To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)

def check_str(s: str):
    """
    Add your code here
    """
    # Remove spaces and convert to lowercase and special characters
    s = ''.join(e for e in s if e.isalnum()).lower()
    print(s)
    print(s[::-1])
    if s == s[::-1]:
        return True
    else:
        return False