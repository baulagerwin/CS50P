def main():
    letters = input("camelCase: ")
    
    for letter in letters:
        if letter.isupper():
            letter = letter.replace(letter, "_" + letter.lower())
            
        print(letter, end="")
    
main()