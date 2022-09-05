def main():
    grocery_list = {}
    
    while True:
        try:
            item = input().strip().upper()
            
            if item not in grocery_list:
                grocery_list[item] = 1
            else:
                grocery_list[item] = grocery_list[item] + 1
        except KeyError:
            pass
        except EOFError:
            grocery_list = {k: v for k, v in sorted(grocery_list.items())}
            break
    
    for grocery in grocery_list:
        print(grocery_list.get(grocery), grocery)
main()