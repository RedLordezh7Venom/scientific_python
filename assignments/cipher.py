'''The first kind of cipher  to build is called a Caesar cipher.
 take each letter in the message, find its position in the alphabet,
   take the letter located after 3 positions, and replace the original letter with the new letter.'''

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
'''
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)
'''
