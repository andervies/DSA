ALPHA_LENGTH = 26
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def decipher_ceasar(key, cipher_text):
    plaintext = ""

    for letter in cipher_text:
        print(letter)
        index = alphabet.index(letter)
        shifted_index = (index - key) % ALPHA_LENGTH
        plaintext += alphabet[shifted_index]

    return plaintext


class Caesar:

    def cipher(self, plain_text, key):
        cipher_text = ""

        for char in plain_text.encode("ascii"):
            if char >= 65 and char < 91:
                numm =(char - 65 + key) % 26
                cipher_text += chr(numm+65)
            elif char >= 97 and char < 123:
                numm = (char - 97 + key) % 26
                cipher_text += chr(numm + 97)
            else:
                cipher_text += chr(char)
        return cipher_text

    def decipher(self, cipher_text, key):
        plain_text = ""

        for char in cipher_text.encode("ascii"):
            if char >= 65 and char < 91:
                numm = (char - 65 - key) % 26
                print(numm)
                plain_text += chr(numm + 65)
            elif char >= 97 and char < 123:
                numm = (char - 97 - key) % 26
                plain_text += chr(numm + 97)
            else:
                plain_text += chr(char)
        return plain_text


caesar = Caesar()
cipher_text = caesar.cipher("Welcome to the internet! have a look around", 4)
plain_text = caesar.decipher(cipher_text, 4)

print(cipher_text)
print(plain_text)