letter = 'a'
ascii_code = ord(letter)
letter_res = chr(ascii_code)
print ascii_code, letter_res
#Intro to Caesar Cipher       
phrase = raw_input("Enter sentence to encrypt: ")
encoded_phrase = ''
shift = int(input("Enter shift value between 1 and 26: "))
for c in phrase:
    if c.isalpha(): #Checks to see if it's alphabetic
        num = ord(c) #Gets ascii value
        num += shift #Shifts the value
        if c.isupper(): #Checks the capitalization
            if num > ord('Z'):
                num -= 26 #Adjusts to get value in range of alphabet
            elif num < ord('A'):
                num += 26
        elif c.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num+= 26
        encoded_phrase += chr(num) #Adds shifted letter
    else:
        encoded_phrase += c
print "The encoded phrase is: ", encoded_phrase
