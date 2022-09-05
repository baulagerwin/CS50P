def main():
    letters = input().strip()
    output = shorten(letters)
    print(f"Output: {output}")


def shorten(letters):
    output = ""
    vowels = "AEIOUaeiou"
    
    for letter in letters:
        for vowel in vowels:
            if letter == vowel:
                letter = letter.replace(letter, "")
                
        output = output + letter
    return output

if __name__ == "__main__":
    main()