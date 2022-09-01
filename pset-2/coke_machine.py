# prompts the user to insert coin one at a time

# prints the amount due until it reaches the amount due

# prints the change owed

def main():
    amount_due = 50

    while True:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        
        if coin == 5 or coin == 10 or coin == 25:
            amount_due = amount_due - coin
            
            if amount_due <= 0:
                print("Change Owed: " + str(abs(amount_due)))
                break;
    
main()