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
    ...

def videoType():
    # Promt the user to choose one of the following options
    print("""Choose one of the following numbers to specifiy the type of file to download
1. (NOT IMPLEMENTED) Audio Only
2. Adaptive (Audio & Video split) [Highest Resolution]
3. (NOT IMPLEMENTED) Progressive (Audio & Video in 1 file) [NOT HIGHEST QUALITY]""")
    
    downloadType = input("Number: ")

    decorationPrints()


# Gets the path for the download folder
def getFolderPath():
    downloadFolderPath = input("Enter download folder path: ").strip('"')
    print(f'DOWNLOAD PATH: {downloadFolderPath}')
    decorationPrints()
    return downloadFolderPath


# Downloads the video!
# To add choice, add an extra argument and if-else statements to 
# change the last method
def downloadVideo(link: str, downloadPath: str): 
    video =  YouTube(link).streams.get_highest_resolution()
   
    try:
        video.download(downloadPath)
    except:
        print("Error!!")


# MAIN METHOD
def main():

    decorationPrints()
    videoType()
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