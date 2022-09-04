def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print("Yes") if answer == "42" or answer == "forty-two" or answer == "forty two" else print("No")

main()