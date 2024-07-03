import random

def PasswordGenerator(length,
                      includeLowerChars,
                      includeUpperChars,
                      inludeNumbers,
                      includeSymbols):
    
    LowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
    UpperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "0123456789"
    Symbols = "!@#$%^&*?~"

    AllowedChars = ""
    Password = ""

    if includeLowerChars :
        AllowedChars += LowerCaseLetters
    
    if includeUpperChars :
        AllowedChars += UpperCaseLetters

    if inludeNumbers :
        AllowedChars += Numbers
    
    if includeSymbols :
        AllowedChars += Symbols

    for i in range(length):
        Password += random.choice(AllowedChars)
    
    return Password

def PasswordCustomization():

    includeLowerCaseLetters = False
    includeUpperCaseLetters = False
    includeNumbers = False
    includeSymbols = False

    length = int(input("Enter the length of password you need to generate: "))

    # Input choices for character types
    choice = input("Include Lowercase Letters? (y/n): ").lower()
    if choice == 'y':
        includeLowerCaseLetters = True

    choice = input("Include Uppercase Letters? (y/n): ").lower()
    if choice == 'y':
        includeUpperCaseLetters = True

    choice = input("Include Numbers? (y/n): ").lower()
    if choice == 'y':
        includeNumbers = True

    choice = input("Include Symbols? (y/n): ").lower()
    if choice == 'y':
        includeSymbols = True
    
    Password = PasswordGenerator(Length,
                      inludeLowerCaseLetters,
                      inludeUpperCaseLetters,
                      Numbers,
                      Symbols
                      )
    print(f'Generated password : {Password}')

PasswordCustomization()
