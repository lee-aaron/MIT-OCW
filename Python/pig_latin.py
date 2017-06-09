raw = raw_input("Enter a word: ")
VOWELS = ['a','e','i','o','u']
if raw[:1] in VOWELS:
    print raw[1:] + raw[:1] + "ay"
else:
    print raw + "hay"
