# @author : Abhiram

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


class VideoType:
    def __init__(self):
        pass

    # Promt the user to choose one of the following options
    def chooseType(self):
        print("Choose one of the following numbers to specifiy the type of file to download\n1. (NOT IMPLEMENTED) Audio Only Best\n2. Audio Only 50kbps\n3. Highest Resolution\n4. 1080p\n5. 720p\n")
        self.type = input("Number: ")
        decorationPrints()

    def getType(self):
        return self.type


# Get only the sources that match with chosen type
class VideoFilter:
    def __init__(self, type, link):
        self.type = type
        self.link = link

    def filter(self):
        if type == 1:              # Audio only best
            return YouTube(self.link).streams.filter(type = "audio").first()
        elif type == 2:            # 50kbps audio only
            itag = 249
            return YouTube(self.link).streams.get_by_itag(itag)
        elif type == 3:            # Highest resolution
            return YouTube(self.link).streams.filter(progressive = True, file_extension = "mp4").first()
        elif type == 4:            # 1080p video
            itag = 137
            return YouTube(self.link).streams.get_by_itag(itag)
        elif type == 5:            # 720p video
            itag = 136
            return YouTube(self.link).streams.get_by_itag(itag)
        else:
            print("Invalid choice!!")
            return None


class Downloader():
    def __init__(self):
        pass

    def download(self, video, downloadPath):
        try:
            video.download(downloadPath)
        except:
            print("Error!!")

        

# Gets the path for the download folder
def getFolderPath():
    downloadFolderPath = input("Enter download folder path: ").strip('"')
    print(f'The DOWNLOAD PATH is: {downloadFolderPath}')
    decorationPrints()
    return downloadFolderPath


# MAIN METHOD
def main():

    # Ask user to choose type of video to download & Get the type of video to download
    decorationPrints()
    VideoType().chooseType() 
    type = VideoType().getType()

    # Ask user to select download folder & Read URLs from file, stored in a list 
    decorationPrints()
    downloadFolderPath = getFolderPath()
    urls = ReadURLs().readURLs()

    # Iterate through list of URLs and download each video
    decorationPrints()
    for url in urls:
        VideoFilter(type, url).filter().download(downloadFolderPath)
    print("ALL VIDEOS DOWNLOADED!!")
    decorationPrints()

if __name__ == '__main__':
    main()