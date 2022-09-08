import re
import sys

def main():
    print(convert(input("Hours: ")))

# 9 AM to 5 PM -> 09:00 to 17:00
# 9:00 AM to 5:00 PM -> 09:00 to 17:00
# 10 PM to 8 AM -> 10:00 to 08:00
# 10:30 PM to 8:50 AM -> 22:30 to 08:50
# 9:60 AM to 5:60 PM -> ValueError
# 9 AM - 5 PM -> ValueError
# 09:00 AM - 17:00 PM -> ValueError

def convert(s):
    if match := re.search(r"(?P<start>[1]?\d(:[0-5][0-9])?) (?P<s_meridian>[AMP]{2}) to (?P<end>[1]?\d(:[0-5][0-9])?) (?P<e_meridian>[AMP]{2})", s):
        start = match.group("start")
        end = match.group("end")
        s_meridian = match.group("s_meridian")
        e_meridian = match.group("e_meridian")
        
        first_part = transform(start, s_meridian)
        second_part = transform(end, e_meridian)
        
        return f"{first_part} to {second_part}"
    raise ValueError

def transform(time, meridian):
    if ":" not in time and meridian == "AM":
        if time == "12":
            time = "00"
        return f"0{time}:00" if len(time) == 1 else f"{time}:00"
    if ":" not in time and meridian == "PM":
        military_hr = str(int(time) + 12)
        if military_hr == "24":
            military_hr = "12"
        return f"{military_hr}:00"
    
    if ":" in time:
        hr, min = time.split(":")
    
    if ":" in time and meridian == "AM":
        if hr == "12":
            return f"00:{min}"
        return f"0{time}" if len(hr) == 1 else time
    if ":" in time and meridian == "PM":
        if hr == "12":
            return time
        military_hr = str(int(hr) + 12)
        return f"{military_hr}:{min}"
        
    raise ValueError

if __name__ == "__main__":
    main()