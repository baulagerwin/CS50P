# def main():
#     yell(["This", "is", "CS50"])


# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     # accumulate
#     print(*uppercased)
    
def main():
    yell("This", "is", "CS50")

# # many arguments
# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# def main():
#     yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()