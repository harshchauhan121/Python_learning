alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



length=len(alphabet)
def encrypt(original_msj,shift_amount):
    encrypted_text=""
    for i in original_msj:
        encrypted_text+= alphabet[(alphabet.index(i)+shift_amount)%26]
    print(encrypted_text)

encrypt(text,shift)



