
def xor_cipher(text,key):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        char_code = ord(text[i])
        key_char_code = ord(key[i% key_length])
        xor_result = char_code ^ key_char_code
        result.append(chr(xor_result))
    return " ".join(result)

plain_text = input("Enter message:")
key = "SECRET"

encrypted_text = xor_cipher(plain_text,key)
print(f"Original plaintext: {plain_text}")
print(f"Encrypted text: {encrypted_text}")

decrypted_text = xor_cipher(encrypted_text,key)
print(f"Decrypted text: {decrypted_text}")