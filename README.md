# Caesar Cipher Encryption/Decryption Tool :eyes:

This is a simple Python program that allows users to encrypt and decrypt messages using the Caesar cipher algorithm. The program provides a command-line interface to input messages and shift values for the encryption and decryption process.

## Features :dizzy:
- Encrypt messages using a specified shift value.
- Decrypt messages using the same shift value used for encryption.
- Supports both uppercase and lowercase letters.
- Retains non-alphabetic characters (such as punctuation and spaces) in the original message.
## How It Works  🤔
The Caesar cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. The same shift is used for both encryption and decryption, but in the opposite direction for decryption.

## Code Explanation  🦾🦾
### Functions
- Encrypt is a function which takes plain text and key and processes the 
-  In the same way Decrypt will do the Opposite to Encrypt function this is 2 way detailed algorithm. 

## Main Logic  
### &nbsp; For Encryption : 
``` python
def Encrypt(text, key):
  cipher_text = ''
  for i in text:
    i = i.lower()
    if not i == ' ':
      index = alphabets.find(i)
      if index == -1:
        cipher_text += i
      else:
        r_index = (index + key) % n
        cipher_text += alphabets[r_index]
  return cipher_text
```

### &nbsp; For Decryption : 
``` python 
def Decrypt(ctext, key):
  plain_text = ''
  for i in ctext:
    i = i.lower()
    if not i == ' ':
      index = alphabets.find(i)
      if index == -1:
        plain_text += i
      else:
        r_index = (index - key) % n
        plain_text += alphabets[r_index]
  return plain_text
```

### Requirements :👍
- python Installed
- Caesar__Cipher.py file
