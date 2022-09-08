import re
import sys


def main():
    print(parse(input("HTML: ")))

# ?(?=\") -> hack to limit a greedy operator
# \" -> limit greedy operator until this character (note that i used escape sequence)
def parse(s):
    if match := re.search(r"^<iframe.*src=\"(?P<URL>.*?(?=\"))\".*></iframe>$", s):
        url = match.group("URL")
        if match_url := re.search(r"^(http|https)://(www.)?youtube.com/embed/(?P<video_code>.*)", url):
            new_url = match_url.group("video_code")
            return f"https://youtu.be/{new_url}"

if __name__ == "__main__":
    main()