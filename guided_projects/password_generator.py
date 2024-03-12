#Regex with password generator
import secrets
import re
import string

def generate_password(length = 16, nums = 1, special_chars = 1 , uppercase = 1 , lowercase = 1):
    #Define the possible character for the password     
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    #Combine all the characters
    all_characters=letters+symbols+digits

    while True:
        password =''    
        #Generate password
        for _ in range(length):
            password +=secrets.choice(all_characters)
    
        constraints = [
            (nums, r'[0-9]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]'),
            (special_chars,fr'[{symbols}]')
        ]

        if all(
            constraint <=len(re.findall(pattern,password))
            for constraint,pattern in constraints
        ):
            '''Having all([expression for i in iterable]), means that a new list is created by evaluating expression for each i in iterable. 
After the all() function iterates over the newly created list, the list is deleted automatically, since it is no longer needed.
Memory can be saved by using a generator expression.
Generator expressions follow the syntax of list comprehensions but they use parentheses instead of square brackets.'''
            break
    return password

''' __name__ == '__main__'. In this way, your code won't run when imported as a module'''
if __name__ == '__main__':
    new_password = generate_password()
    print(new_password)
