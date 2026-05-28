alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z',' '
]
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]
    print(f"Here is the encoded result: {cipher_text}")
def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet)
        output_text += alphabet[shift_position]
    print(f"Here is the decoded result: {output_text}")
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        output_text += alphabet[shift_position]
    print(f"Here is the final result: {output_text}")
encrypt(original_text=text, shift_amount=shift)
decrypt(original_text=text, shift_amount=shift)
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
