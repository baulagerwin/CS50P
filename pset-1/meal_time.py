def main():
    time = input("What time is it? ")
    print(is_meal_time(convert(time)))
    
def convert(time):
    if time.endswith("a.m."):
        total_hours = time_to_total_hours(time)
        return total_hours if total_hours >= 7 and total_hours <= 8 else -1
        
    elif time.endswith("p.m."):
        total_hours = time_to_total_hours(time)
        return standard_time_to_military_time(total_hours)

    else:   
        return time_to_total_hours(time)
    
def is_meal_time(total_hours):
    if total_hours >= 7 and total_hours <= 8:
        return "breakfast time"
    
    elif total_hours >= 12 and total_hours <= 13:
        return "lunch time"
    
    elif total_hours >= 18 and total_hours <= 19:
        return "dinner time"
    
    else:
        return ""
    
def time_to_total_hours(time):
    if time.endswith("a.m.") or time.endswith("p.m."):
        hr_mins, am_pm = time.split(" ")
        hr, mins = hr_mins.split(":")
        
    else:
        hr, mins = time.split(":")
        
    hr = float(hr)
    mins = float(mins)
    mins_to_hr = mins / 60
    
    return hr + mins_to_hr

def standard_time_to_military_time(total_hours):
    military_number = 12
        
    if total_hours >= 12 and total_hours < 13:
        return total_hours
    elif total_hours == 1:
        return total_hours + military_number
    elif total_hours >= 6 and total_hours <= 7:
        return total_hours + military_number
    else:
        return -1

main()