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

print(decipher_ceasar(7, "khhspkhylfvbavjylhalhjhlzhyjpwolykljyfwapvuhsnvypaotbzpunhnpclurlf"))