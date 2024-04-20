import re




def parse(code):
    if youtube_link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", code):
        return f"https://youtu.be/{youtube_link.group(2)}"
    else:
        return None



def main():
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()