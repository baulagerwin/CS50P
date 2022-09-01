def main():
    # prompts the user for an arithmetic expression
    expression = input("Arithmetic Expression: ").strip().lower()
    
    # splits the expression
    x, y, z = expression.split(" ")
    
    # cast x and y
    x = float(x)
    z = float(z)
    
    # control and calculate the expression
    match y:
        case "+":
            print(f"{x + z:.1f}")
        case "-":
            print(f"{x - z:.1f}")
        case "*":
            print(f"{x * z:.1f}")
        case "/":
            print(f"{x / z:.1f}")
        case "%":
            print(f"{x % z:.1f}")
        case _:
            print("Invalid arithmetic expression")
    
main()