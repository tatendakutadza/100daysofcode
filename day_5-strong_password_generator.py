# Strong Password Generator

import string
import random
import logging

logging.basicConfig(filename='password_generator.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s:')

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list(string.punctuation)
list_with_everything = lowercase_letters + uppercase_letters + digits + special_characters

password_length = int(input("How many characters do you want your password to have: "))
password_list = []

while len(password_list) < password_length:
    password_char = random.choice(list_with_everything)
    if password_char in ['!', '"', "'", '(', ')', ',', '-', '.', '/', ':', ';', '=', '[', '\\', ']',
                         '`', '~', '{', '|', '}']:
        continue
    else:
        password_list.append(password_char)

password = ''.join(password_list)
print("Generated password: {}".format(password))
logging.debug("Password generated: {}".format(password))
