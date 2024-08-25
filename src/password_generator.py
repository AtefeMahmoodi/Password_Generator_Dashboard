import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    """Main class for generating passwords.
    
    """
    @abstractmethod
    def generate(self):
        """
        Subclasses should override this method to generate password.
        """
        pass

class MemorablePasswordGenerator(PasswordGenerator):
    """Class for generating memorable random password. This is a subclass of PasswordGenerator

    """
    def __init__(self,number_of_words=4, separator='-', capitalize=False, vocabulary=None):
        """Method to initialize the parameters.

        :param number_of_words: How many words must exist in the password, defaults to 4
        :type number_of_words: int, optional
        :param separator: The words must be separated by which punctuation, defaults to '-'
        :type separator: str, optional
        :param capitalize: Must the password include words with capital letters, defaults to False
        :type capitalize: bool, optional
        :param vocabulary: The list of words from which the password must be chosen, defaults to None
        :type vocabulary: _type_, optional
        """
        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalize = capitalize
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()
        else:
            self.vocabulary = vocabulary

    def generate(self):
        """Generate a password from specified word list.

        :return: random memorable password
        :rtype: str
        """
        password = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            password = [word.capitalize() if random.choice([True,False]) else word.lower() for word in password]
        return self.separator.join(password)

class RandomPasswordGenerator(PasswordGenerator):
    """Class for generating random passwords. Numbers and punctuations can be included. This is a subclass of PasswordGenerator.

    """
    def __init__(self, length=8, include_numbers=True, include_symbols=True):
        """Method to initialize the parameters.

        :param length: How long must the password be, defaults to 8
        :type length: int, optional
        :param include_numbers: Must the password include the numbers, defaults to True
        :type include_numbers: bool, optional
        :param include_symbols: Must the password include the puctuations, defaults to True
        :type include_symbols: bool, optional
        """
        self.length = length
        self.all_choices = string.ascii_letters
        if include_numbers:
            self.all_choices += string.digits
        if include_symbols:
            self.all_choices += string.punctuation
        
    
    def generate(self):
        """Generate a password from specified characters.

        :return: random password
        :rtype: string    
        """
        return ''.join([random.choice(self.all_choices) for _ in range(self.length)])

class PinCodeGenerator(PasswordGenerator):
    """Class for generaing pincode. This is a subclass of PasswordGenerator."""
    def __init__(self, length=8):
        """Method to initialize the parameters.

        :param length: How long must the password be, defaults to 8
        :type length: int, optional
        """
        self.length = length
    
    def generate(self):
        """Generate pincode of the specified length.

        :return: pincode
        :rtype: string
        """
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


# def main():
#     pin = PinCodeGenerator(length = 10)
#     random_pass = RandomPasswordGenerator(length = 12, include_symbols = False)
#     memorable = MemorablePasswordGenerator(number_of_words=4, capitalize=True, separator='*')
#     print(f"This is a random password: {random_pass.generate()}")
#     print(f"This is a random pin code: {pin.generate()}")
#     print(f"This is a memorable password: {memorable.generate()}")

# if __name__ == "__main__":
#     main()
