def header(title):
    print()
    print(20 * '-')
    print(title)

def encode_text(symbols, message, shifts):
    encryption = ""
    for letter in message:
        letter_idx = symbols.index(letter)
        if ((letter_idx + shifts) // 26) > 0:
            new_idx = (letter_idx + shifts) - (((letter_idx + shifts) // 26) * 26)
            shifted_letter = symbols[new_idx]
            encryption += shifted_letter
        else:
            shifted_letter = symbols[letter_idx + shifts]
            encryption += shifted_letter
    header("RESULT\n")
    print(f"Encrypted message: {encryption}")

def decode_text(symbols, message, shifts):
    decryption = ""
    for letter in message:
        letter_idx = symbols.index(letter)
        if (letter_idx - shifts) < 0:
            new_idx = (letter_idx - shifts) + ((abs(letter_idx - shifts) // 26) * 26)
            shifted_letter = symbols[new_idx]
            decryption += shifted_letter
        else:
            shifted_letter = symbols[letter_idx - shifts]
            decryption += shifted_letter
    header("RESULT\n")
    print(f"Decrypted message: {decryption}")

def continue_or_stop():
    while True:
        header("CONTINUE OR EXIT\n")
        user_input = input("Would you like to encrypt/decrypt again? (y/n): ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            return True
        elif user_input.lower() == "n" or user_input.lower() == "no":
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please try again.")