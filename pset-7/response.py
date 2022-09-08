import validators

def main():
    print(validate(input("Text: ")))

def validate(s):
    return "Valid" if validators.email(s) else "Invalid"

if __name__ == "__main__":
    main()