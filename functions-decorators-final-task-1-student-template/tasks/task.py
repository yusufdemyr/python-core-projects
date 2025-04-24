# ## Functions. Decorators. Final Task 1.

# Implement a function that works the same as `str.split` method
# (without using `str.split` itself, ofcourse).
# Pay attention to strings with multiple spaces. For example: '    Hi     Python    world!' 

# Example:
# ```python
#     def split(data: str, sep=None, maxsplit=-1):
#         ...


from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if not data:
        return []

    result = []
    current = ''
    count = 0
    i = 0
    length = len(data)

    if sep is None:
        if maxsplit == 0:
            return [data.strip()]
        
        in_token = False
        while i < length:
            if data[i].isspace():
                if in_token:
                    result.append(current)
                    current = ''
                    in_token = False
                    count += 1
                    if 0 <= maxsplit == count:
                        break
            else:
                current += data[i]
                in_token = True
            i += 1
        if current:
            result.append(current)
        if 0 <= maxsplit == count and i < length:
            remainder = data[i:].lstrip()
            if remainder:
                result.append(remainder)

    else:
        while i < length:
            if maxsplit != -1 and count == maxsplit:
                result.append(data[i:])
                break
            if data[i:i+len(sep)] == sep:
                result.append(current)
                current = ''
                i += len(sep)
                count += 1
            else:
                current += data[i]
                i += 1
        else:
            result.append(current)

    return result

    
if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']