# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted


ciphertext = ""

decrypted_msg = cipher_decrypt(ciphertext,1)

print("The cipher text:\n", ciphertext)

print("The decrypted message is:\n",decrypted_msg)






