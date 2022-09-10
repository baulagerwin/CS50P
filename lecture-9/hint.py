def meow(n: int) -> str:
    return "meow\n" * n

# Sphinx library
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")