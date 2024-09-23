
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c','d', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = shift_amount + position
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")

from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input('Type "encode" for encrypt, "decode" for decrypt: \n')
    text = input("Type your message: \n").lower()
    shift= int(input("Type the shift num: \n"))
    shift %= 26

    ceaser(start_text= text, shift_amount=shift, cipher_direction=direction)

    ask= input("Do you want to restart the program? Type 'Yes' if yes or 'No' if no \n" ).lower()
    if ask == "no":
        should_continue = False
        print("GooodBye!")


