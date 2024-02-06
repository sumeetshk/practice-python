msg = input("Enter your message to encrypt: ")


def encrypt(msg):
    result = ""

    # iterate through the input msg
    for i in range(len(msg)):
        char = msg[i]
        print(char)
        # Check if character is alphanumeric
        if char.isalpha():
            # Check char is either Z or z and append A, a respectively
            if char == 'Z':
                result += 'A'
            elif char == 'z':
                result += 'a'

            # Else shift to the next letter
            else:
                result += chr((ord(char) + 1))

        # If char not alphanumeric just continue
        else:
            result += char
    return result


print("Message to encrypt : ", msg)
print("Cipher: ", encrypt(msg))
