alphabets = "abcdefghijklmnopqrstuvwxyz"
n = len(alphabets)

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

print('CAESAR CIPHER')
print()
print("Hi! What's your task?")
print("Encrypt/Decrypt")
print("E for Encrypt")
print("D for Decrypt")
ch = input().upper()  
print()

if ch == 'E':
  print("Encryption Mode ON!!!!!!!!!!!")
  print()
  while True:  # Loop for input validation (key value)
    try:
      key = int(input("Enter a key Value 1-26: "))
      if 1 <= key <= 26:
        break
      else:
        print("Invalid key. Please enter a value between 1 and 26.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  text = input("Enter Text to Encrypt")
  cipher_text = Encrypt(text, key)
  print(f'CIPHER TEXT:{cipher_text}')

elif ch == 'D':
  print("Decryption Mode ON!!!!!!!!!!!")
  print()
  while True:  # Loop for input validation (key value)
    try:
      key = int(input("Enter a key Value 1-26: "))
      if 1 <= key <= 26:
        break
      else:
        print("Invalid key. Please enter a value between 1 and 26.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  ctext = input("Enter Text to Decrypt")
  plain_text = Decrypt(ctext, key)
  print(f'PLAIN TEXT: {plain_text}')

else:
  print('Enter Correct Choice')
