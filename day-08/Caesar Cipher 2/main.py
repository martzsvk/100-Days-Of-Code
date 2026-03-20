alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text,shift):
    original_text = list(text)
    if direction == "encode":
        for letter in original_text:
            index = alphabet.index(letter)
            shift_amount = index + shift
            print(alphabet[shift_amount],sep='',end='',flush=True)
    elif direction == "decode":
        for letter in original_text:
            index = alphabet.index(letter)
            shift_amount = index - shift
            print(alphabet[shift_amount],sep='',end='',flush=True)
    else:
        print("Incorrect requirement. ")

ceaser(text,shift)







