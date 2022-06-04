#Program that encodes/decodes a message in morse code
#!/usr/bin/env python3

#dictionary with key pair values for morse
#probably a better way to write this
MORSE_CODE = { 'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-...',  'e': '.',
               'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.----',
               'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
               'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
               'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
               'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
               '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
               '0': '-----'}

def main():
    myMsg = "SOS This is the 1st test!"
    myMsg2 = "... --- ... - .... .. ... .. ... - .... . .---- ... - - . ... -"

    print(encodeMorse(myMsg))
    print(decodeMorse(myMsg2))

def encodeMorse(msg):
    #make every character lowercase in the string
    msg = msg.lower()
    coded_msg = ''

    #encode the message into morse
    for character in msg:
        if character in MORSE_CODE:
            coded_msg += MORSE_CODE[character] + " "
        else:
            coded_msg += character

    return coded_msg

def decodeMorse(msg):
    decoded_msg = ""
    message = msg.split()
    ENCODED_MORSE = {}
    to_replace = { "{": "", "}": "", "\'": ""}

    #create a new dict with the key being dashes and dots
    #and the value being the leter or number
    for key, value in MORSE_CODE.items():
        ENCODED_MORSE[value] = {key}

    #if the morse code enter matches the dict the put the
    #letter value into decoded_msg. ignore other chars that are
    #not A-Z or 0-9
    for char in message:
        if char in ENCODED_MORSE:
            decoded_msg += str(ENCODED_MORSE[char])
        else:
            decoded_msg += char

    #each letter is saved like this {'a'} so the unnecessary
    #characters are removed - { } '
    for key, value in to_replace.items():
        decoded_msg = decoded_msg.replace(key,value)

    return(decoded_msg)

if __name__ == '__main__':
    main()
