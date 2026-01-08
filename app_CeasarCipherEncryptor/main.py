import utils as u

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

start_app = True # Flag to keep app going until user chooses to exit
while start_app == True:
    u.header("CHOOSE AN OPTION\n")
    encode_or_decode = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    print()
    message = input("Please enter your message: ")
    shift_amount = int(input("Please enter the shift value: "))

    if encode_or_decode.lower() == "encode":
        u.encode_text(alphabet, message, shift_amount)
        start_app = u.continue_or_stop()

    elif encode_or_decode.lower() == "decode":
        u.decode_text(alphabet, message, shift_amount)
        start_app = u.continue_or_stop()

    else:
        print("Invalid choice. Please try again.")

