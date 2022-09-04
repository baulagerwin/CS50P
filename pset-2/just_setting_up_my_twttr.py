# prompts the user for a text

# outputs the same text but without A, E, I, O, U

def main():
    letters = input("Input: ").strip()
    output = ""
    vowels = "AEIOUaeiou"
    
    for letter in letters:
        for vowel in vowels:
            if letter == vowel:
                letter = letter.replace(letter, "")
                
        output = output + letter
    
    print(f"Output: {output}")

main()