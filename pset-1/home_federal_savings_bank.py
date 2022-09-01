def main():
    # accepts greeting
    greeting = input("Greeting: ").strip().lower()

    # if greeting starts with "hello" output $0
    if greeting.startswith("h") and greeting.startswith("hello"):
        print("$0")
    # if greeting starts with "h" output $20
    elif greeting.startswith("h"):
        print("$20")
    # else output $100
    else:
        print("$100")

main()