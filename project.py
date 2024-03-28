import threading
from pytube import YouTube


# Function to print decorative lines
def print_decorative_lines():
    print("------------------------------------------------------")

# Custom Exception class
class TypeNotInRangeException(Exception):
    '''Raised when user input is not in the range of 1-5'''
    pass

# Reads URLs from a file
class URLReader:
    def __init__(self):
        self.urls = []

    # Read URLs from an existing file, 
    # ARGS:    files (str): The path to the file containing URLs. Defaults to "urls.txt".
    # RETURNS: list- A list of URLs read from the file
    def read_urls(self, files="urls.txt"):
        with open(files, 'r') as file:
            urls = file.readlines()
        return urls


# Class to choose the type of video to download
class VideoType:
    def __init__(self):
        pass

    # Prompt the user to choose one of the following options for video type
    def choose_type(self):
        print("Choose one of the following numbers to specify the type of file to download:")
        print("1. Audio Only Best")
        print("2. Audio Only 50kbps")
        print("3. Highest Resolution")
        print("4. 1080p")
        print("5. 720p")
        self.type = int(input("Enter the number: "))
        print_decorative_lines()

    # Validate the type of video chosen by the user
    # Raises TypeNotInRangeException if the type is not in the range of 1-5 
    def validate_type(self):
        if self.type not in range(1,6):
            raise TypeNotInRangeException("Input not in the range of 1-5!")

    # Get the type of video chosen by the user
    def get_type(self):
        return self.type

# Function to filter the video based on the type chosen by the user
# ARGS:    video_type (str): The type of video chosen by the user
#          link (str): The URL of the video
# RETURNS: source (pytube.Stream): The source of the video to be downloaded
def filter(video_type, link):
    if video_type == 1:              # Audio only best
        return YouTube(link).streams.filter(type="audio").first()
    elif video_type == 2:            # 50kbps audio only
        return YouTube(link).streams.get_by_itag(249)
    elif video_type == 3:            # Highest resolution
        return YouTube(link).streams.filter(progressive=True, file_extension="mp4").first()
    elif video_type == 4:            # 1080p video
        return YouTube(link).streams.get_by_itag(137)
    elif video_type == 5:            # 720p video
        return YouTube(link).streams.get_by_itag(136)
    else:
        print("Invalid choice!!")


# Function to get the path for the download folder
def get_folder_path():
    download_folder_path = input("Enter download folder path: ").strip('"')
    print(f'The DOWNLOAD PATH is: {download_folder_path}')
    print_decorative_lines()
    return download_folder_path

# Function to download the video
# ARGS:    url (str): The URL of the video
#          video_type (str): The type of video chosen by the user
#          download_folder_path (str): The path of the download folder
# RETURNS: None
def download_video(url, video_type, download_folder_path): 
    try:
        source = filter(video_type, url.strip())
        if source:
            source.download(download_folder_path)
        else:
            print(f"No suitable source found for URL: {url.strip()}")
    except Exception:
        print(f"Error downloading video from URL: {url.strip()}")
    print("ALL VIDEOS DOWNLOADED!!")
    print_decorative_lines()


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
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_video, args=(url, video_type, download_folder_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
