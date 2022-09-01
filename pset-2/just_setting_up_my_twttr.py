# prompts the user for a text

# outputs the same text but without A, E, I, O, U

def main():
    text = input().strip()
    
    for letter in text:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            letter = letter.replace(letter, "")
            
        print(letter, end="")
    
main()