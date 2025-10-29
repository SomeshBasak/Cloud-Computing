
def caesar_cipher_encrypt(plain_text, shift):
    cipher_text = " "

    for char in plain_text:
        if char.isalpha():
            start_ascii = ord("a") if char.islower() else ord("A")
            shifted_char_ascii = (ord (char) - start_ascii + shift) % 26 + start_ascii
            cipher_text += chr(shifted_char_ascii)
        else:
            cipher_text += char
    return cipher_text

message = input("Enter the message:")
shift_value = int(input("Enter the shift value:"))
encrypted_message = caesar_cipher_encrypt(message, shift_value)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")