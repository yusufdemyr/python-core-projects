# # Final tasks. Task 2

# Implement the keyword encoding and decoding for the Latin alphabet.
# The keyword cipher uses a keyword to rearrange the letters in the alphabet.
# You should add the provided keyword at the beginning of the alphabet.
# A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. 
# The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up,
#  whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# **Encryption:**

# *The keyword is "Crypto"*

# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z



# **Example:**
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
# ```

class Cipher:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self,keyword):
        self.keyword = keyword
        self.cipher_alphabet = self._create_cipher()


        
    def encode(self, data):
        data = data.upper()

        translation_table = str.maketrans(self.alphabet, self.cipher_alphabet)
        return data.translate(translation_table).lower().capitalize()
    
    def decode(self, data):
        data = data.upper()

        translation_table = str.maketrans(self.cipher_alphabet, self.alphabet)
        return data.translate(translation_table).lower().capitalize()
    
    def _create_cipher(self):
        keyword = self.keyword.upper()
        cipher_alphabet = keyword + "".join(sorted(set(self.alphabet) - set(keyword)))
        return cipher_alphabet

