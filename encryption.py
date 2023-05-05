# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for a in plain_text:

        if a.isupper(): #check if it's an uppercase character

            a_index = ord(a) - ord('A')

            # shift the current character by key positions
            a_shifted = (a_index + key) % 26 + ord('A')

            a_new = chr(a_shifted)

            encrypted += a_new

        elif a.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            a_index = ord(a) - ord('a') 

            a_shifted = (a_index + key) % 26 + ord('a')

            a_new = chr(a_shifted)

            encrypted += a_new

        elif a.isdigit():

            # if it's a number,shift its actual value 
            a_new = (int(a) + key) % 10

            encrypted += str(a_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += a

    return encrypted
    
plain_text = ""

ciphertext = cipher_encrypt(plain_text, 1)

print("Plain text message:\n", plain_text)

print("Encrypted ciphertext:\n", ciphertext)

