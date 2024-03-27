from pytube import YouTube

# Function to print decorative lines
def print_decorative_lines():
    print("------------------------------------------------------")

# Custom Exception class
class TypeNotInRangeException(Exception):
    "Raised when user input is not in the range of 1-5"
    pass

# Reads URLs from a file
class URLReader:
    def __init__(self):
        self.urls = []

    # Read URLs from an existing file
    def read_urls(self, file_path):
        with open(file_path, 'r') as file:
            urls = file.readlines()
        return urls


# Class to choose the type of video to download
class VideoType:
    def __init__(self):
        pass

    # Prompt the user to choose one of the following options
    def choose_type(self):
        print("Choose one of the following numbers to specify the type of file to download:")
        print("1. (NOT IMPLEMENTED) Audio Only Best")
        print("2. Audio Only 50kbps")
        print("3. Highest Resolution")
        print("4. 1080p")
        print("5. 720p")
        print_decorative_lines()
        try:
            self.type = int(input("Enter the number: "))
            if self.type not in range(1,6):
                raise TypeNotInRangeException
        except TypeError:
            print("Input not in the range of 1-5!")

    def get_type(self):
        return self.type


class VideoFilter:
    def __init__(self, video_type, link):
        self.video_type = video_type
        self.link = link

    def filter(self):
        if self.video_type == '1':              # Audio only best
            return YouTube(self.link).streams.filter(type="audio").first()
        elif self.video_type == '2':            # 50kbps audio only
            itag = 249
            return YouTube(self.link).streams.get_by_itag(itag)
        elif self.video_type == '3':            # Highest resolution
            return YouTube(self.link).streams.filter(progressive=True, file_extension="mp4").first()
        elif self.video_type == '4':            # 1080p video
            itag = 137
            return YouTube(self.link).streams.get_by_itag(itag)
        elif self.video_type == '5':            # 720p video
            itag = 136
            return YouTube(self.link).streams.get_by_itag(itag)
        else:
            print("Invalid choice!!")
            return None


# Function to get the path for the download folder
def get_folder_path():
    download_folder_path = input("Enter download folder path: ").strip('"')
    print(f'The DOWNLOAD PATH is: {download_folder_path}')
    print_decorative_lines()
    return download_folder_path


# MAIN METHOD
def main():
    # Ask user to choose type of video to download & Get the type of video to download
    print_decorative_lines()
    video_type_selector = VideoType()
    video_type_selector.choose_type()
    video_type = video_type_selector.get_type()

    # Ask user to select download folder & Read URLs from file, stored in a list
    print_decorative_lines()
    download_folder_path = get_folder_path()
    urls_reader = URLReader()
    urls = urls_reader.read_urls("urls.txt")

    # Iterate through list of URLs and download each video
    print_decorative_lines()
    for url in urls:
        VideoFilter(video_type, url.strip()).filter().download(download_folder_path)
    print("ALL VIDEOS DOWNLOADED!!")
    print_decorative_lines()


if __name__ == '__main__':
    main()
