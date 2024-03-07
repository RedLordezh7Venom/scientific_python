#The first kind of cipher  to build is called a Caesar cipher.
#take each letter in the message, find its position in the alphabet,
# take the letter located after 3 positions, and replace the original letter with the new letter.

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar("Hello world what's up",5)
