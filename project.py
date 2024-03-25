from pytube import YouTube

# Prints pretty lines for cleaner terminal look
def decorationPrints():
    print("------------------------------------------------------")


class ReadURLs():
    def __init__(self):
        self.urls = []

    # Read URLs from existing file
    def readURLs(self):
        with open("urls.txt", 'r') as file:
            urls = file.readlines()
        return urls


class VideoType():
    def __init__(self):
        pass

    # Promt the user to choose one of the following options
    def chooseType(self):
        print("Choose one of the following numbers to specifiy the type of file to download\n1. (NOT IMPLEMENTED) Audio Only\n2. Adaptive (Audio & Video split) [Highest Resolution]\n3. (NOT IMPLEMENTED) Progressive (Audio & Video in 1 file) [NOT HIGHEST QUALITY]")
        self.type = input("Number: ")
        decorationPrints()

    def getType(self):
        return self.type


# Get only the sources that match with chosen type
class VideoFilter(type):
    def __init__(self, type, link):
        self.type = type

    def filter(self):
        if type == 1:
            return YouTube().streams.filter(only_audio=True)
        elif type == 2:
            return YouTube().streams.filter(only_video=True)
        elif type == 3:
            return YouTube().streams.filter(progressive=True)
        else:
            print("Invalid choice!!")
            return None


class Downloader():
    ...

# Gets the path for the download folder
def getFolderPath():
    downloadFolderPath = input("Enter download folder path: ").strip('"')
    print(f'The DOWNLOAD PATH is: {downloadFolderPath}')
    decorationPrints()
    return downloadFolderPath


# Downloads the video!
def downloadVideo(link: str, downloadPath: str): 
    # video =  YouTube(link).streams.get_highest_resolution()
   
    try:
        video.download(downloadPath)
    except:
        print("Error!!")


# MAIN METHOD
def main():

    decorationPrints()
    # videoType()
    decorationPrints()
    
    # Ask user to select download folder
    downloadFolderPath = getFolderPath()
    
    # Read URLs from file
    urls = ReadURLs().readURLs()

    # Iterate through list of URLs and download each
    for url in urls:
        downloadVideo(url, downloadFolderPath)

    print("ALL VIDEOS DOWNLOADED!!")
    decorationPrints()

if __name__ == '__main__':
    main()