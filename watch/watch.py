import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to find the YouTube URL in an iframe's src attribute
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"', s)
    if match:
        # Extract the video ID from the URL
        url = match.group(1)
        video_id = url.split('/')[-1]
        # Return the short youtu.be version of the URL
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
