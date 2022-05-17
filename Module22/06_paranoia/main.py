import os

text = 'Hello\n'
file_text = open('text.txt','w')
file_text.write(text * 4)
file_text.close()

caesar_file = open('cipher_text.txt', 'w')
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_ceasar(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 25
        return chr(number)
    return letter

step = 0
with open('text.txt') as text:
    for line in text:
        if step == 26:
            step = 0
        else:
            step += 1
        for letter in line:
            result = get_ceasar(letter, step)
            caesar_file.write(result)

file_text.close()
caesar_file.close()





