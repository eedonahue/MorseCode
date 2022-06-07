# !/usr/bin/env python3



# dictionary with key pair values for morse
MORSE_CODE = { 'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-...',  'e': '.',
               'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.----',
               'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
               'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
               'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
               'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
               '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
               '0': '-----'}

def main():
  
    # myMsgTest = "SOS This is the 1st test!"
    # myMsg2Test = "... --- ... - .... .. ... .. ... - .... . .---- ... - - . ... -"

    choice = int(input("-----MENU-----: \n" +
                   "  1. Encode\n" +
                   "  2. Decode \n" +
                   "  What would you like to do: "))
    
    if choice == 1:
      myMsg = input("\n Enter the statement you would like to encode: \n\n ")
      print("\n ** " + encodeMorse(myMsg) + " ** ")
    elif choice == 2:
      myMsg2 = input("\n Enter the statement you would like to decode: \n\n ")  
      print("\n ** " + decodeMorse(myMsg2) + " ** ")
    else:
      print("That is not an option.")
      main()

def encodeMorse(msg):
    # make every character lowercase in the string
    msg = msg.lower()
    coded_msg = ''

    # encode the message into morse
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

    # create a new dict with the key being dashes and dots
    # and the value being the leter or number
    for key, value in MORSE_CODE.items():
        ENCODED_MORSE[value] = {key}

    # if the morse code enter matches the dict the put the
    # letter value into decoded_msg. ignore other chars that are
    # not A-Z or 0-9
    for char in message:
        if char in ENCODED_MORSE:
            decoded_msg += str(ENCODED_MORSE[char])
        else:
            decoded_msg += char

    # each letter is saved like this {'a'} so the unnecessary
    # characters are removed - { } '
    for key, value in to_replace.items():
        decoded_msg = decoded_msg.replace(key,value)

    return(decoded_msg)

if __name__ == '__main__':
    main()
