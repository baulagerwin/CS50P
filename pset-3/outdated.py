from curses.ascii import isdigit

def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    
    while True:
        try:
            anno_domini_date = input("Date: ").strip()
            
            if "/" in anno_domini_date and " " not in anno_domini_date:
                date_splitted = anno_domini_date.split("/")
                validator = [12, 31, 2022]
                
                # checks if its a date
                if len(date_splitted) != 3:
                    raise ValueError
                    
                # checks if the month, day, year are digits
                for number in date_splitted:
                    for digit in number:
                        if not isdigit(digit):
                            raise ValueError
                        
                # checks if the month, day, year are valid
                for i in range(len(date_splitted)):
                    for j in range(len(validator)):
                        if j != i:
                            continue
                        
                        if int(date_splitted[i]) >= 0 and int(date_splitted[i]) <= validator[i]:
                            continue
                        else: raise ValueError
                        
                month, day, year = date_splitted
                
                month = int(month)
                day = int(day)
                year = int(year)
                
            elif " " in anno_domini_date and not "/" in anno_domini_date and anno_domini_date.__contains__(","):
                date_splitted = anno_domini_date.split(" ")
                                
                # checks if its a date
                if len(date_splitted) != 3:
                    raise ValueError
                
                month, day, year = date_splitted
                month = month.title()
                
                if "," in day:
                    day = day.replace(",", "")
                    
                for i in range(len(months)):
                    if month == months[i]:
                        month = i + 1
                
                numbers = [day, year]
                # checks if the month, day, year are digits
                for number in numbers:
                    for digit in number:
                        if not isdigit(digit):
                            raise ValueError
                        
                validator = [31, 2022]
                # checks if the day, year are valid
                for i in range(len(numbers)):
                    for j in range(len(validator)):
                        if j != i:
                            continue
                        
                        if int(numbers[i]) >= 0 and int(numbers[i]) <= validator[i]:
                            continue
                        else: raise ValueError
                
                day = int(day)
                year = int(year)
            else:
                raise ValueError
        except (ValueError):
            pass
        else:
            print(f"{year}-{month:02}-{day:02}")
            break

main()