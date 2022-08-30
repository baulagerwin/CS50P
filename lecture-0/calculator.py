# # Get the user's input
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # Create a rounded result
# z = x / y

# # Print the result
# print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n

main()