def main():
    # accepts greeting
    greeting = input("Greeting: ").strip().lower()
    result = value(greeting)
    print(f"${result}")

def value(greeting):
    # if greeting starts with "hello" output $0
    if greeting.startswith("h") and greeting.startswith("hello"):
        return "0"
    # if greeting starts with "h" output $20
    elif greeting.startswith("h"):
        return "20"
    # else output $100
    else:
        return "100"


if __name__ == "__main__":
    main()