import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_characters = ["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]

again = "yes"
while again == "yes":


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceaser(text,shift):
        cipher_text = " "
        original_text = list(text)
        if direction == "encode":
            for letter in original_text:
                if letter == " " or letter.isnumeric() or letter in special_characters:
                    cipher_text += letter
                else:
                    index = alphabet.index(letter)
                    shift_amount = index + shift
                    cipher_text += alphabet[shift_amount]
            return cipher_text
        elif direction == "decode":
            for letter in original_text:
                if letter == " " or letter.isnumeric() or letter in special_characters:
                    cipher_text += letter
                else:
                    index = alphabet.index(letter)
                    shift_amount = index - shift
                    cipher_text += alphabet[shift_amount]
            return cipher_text
    result = ceaser(text, shift)
    print(result.lstrip())

    again = input("Do you want to continue? 'yes' or 'no' ").lower()
    if again == "no":
        exit()



















