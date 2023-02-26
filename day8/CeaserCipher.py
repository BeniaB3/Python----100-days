from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar_encode(input_text, input_shift, enc_or_dec):
    result = ""
    if enc_or_dec == "encode":
        for letter in input_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + input_shift
                if new_position > 25:
                    new_position = new_position - 26
                result += alphabet[new_position]
            else:
                result += letter


    elif enc_or_dec == "decode":
        for letter in input_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - input_shift
                if new_position < 0:
                    new_position = new_position + 26
                result += alphabet[new_position]
            else:

                result += letter

    print(f"The {enc_or_dec}d text is {result}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_encode(input_text=text, input_shift=shift, enc_or_dec=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
