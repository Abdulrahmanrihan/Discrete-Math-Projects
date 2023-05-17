# Define the alphabet dictionary
alphabet = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

#function to get key using value 
def get_key(val):
    for key, value in alphabet.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# Apply the encryption
def encryption(message):
    encrypted_message = ""       #dy empty string to store the encrypted msg.
    for letter in message:
        # Ignore spaces
        if letter == " ":
            #if there's space in message
            encrypted_message += "  "    #it'll add a space to the encr.
        else:
            # Apply the hash function
            value = (alphabet[letter]+ 11) % 26
            # Append the encrypted letter to the encrypted message
            encrypted_message += str(value) + " "
    print(encrypted_message)

#decryption function
def decryption(numbers):
    
    original_text = "" #empty string to store decrypted msg
    
    for number in numbers.split(" "): #loop over every letter's number in the array
        if number == " " or number == '':
            original_text += " "
        else:
            number = int(number)
            #get key is a function designed to get the key in a dictionary using the corresponding value
            letter = get_key((number - 11) % 26)
            #append the decrypted character to the original text variable
            original_text += letter 
    print(original_text)

# encrypt or decrypt by commenting out one and using the other

encryption( "LOVE ENG FATMA")

decryption("23 0 7 16  16 25 18  17 12 5 24 12")






