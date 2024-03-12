from pytube import YouTube

# Prints pretty lines for cleaner terminal look
def decorationPrints():
    print("------------------------------------------------------")

'''
class DownloadType:

    def __init__(self, type="Highest Resolution"):
        self.type = type

    def normalType():
        ...        

def getItag():
    ##############################################
    this function if implemented will use the terminal to choose which specific 
    file to download from a list of given sources.
    displayed as:
        'itag: <Stream: itag="124" ...>'
    ##############################################

'''


def userInputs():
    # Promt the user to choose XXXXXXX
    print("""Choose one of the following numbers to specifiy the type of file to download
1. (NOT IMPLEMENTED) Audio Only
2. Adaptive (Audio & Video split) [Highest Resolution]
3. (NOT IMPLEMENTED) Progressive (Audio & Video in 1 file) [NOT HIGHEST QUALITY]""")
    
    downloadType = input("Number: ")
    decorationPrints()

    # Prompt user for URLs and store them in a list
    while True:
        url = input("Enter YouTube URL (or 'done' to finish): ")
        if url.lower() == "done":
            break
        urls.append(url)


def getFolderPath():
    downloadFolderPath = input("Enter download folder path: ").strip('"')
    print(f'DOWNLOAD PATH {downloadFolderPath}')
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
    global urls
    urls = []

    decorationPrints()
    userInputs()
    decorationPrints()
    
    # Ask user to select download folder
    downloadFolderPath = getFolderPath()
    
    # Iterate through list of URLs and download each
    for url in urls:
        downloadVideo(url, downloadFolderPath)

    print("ALL VIDEOS DOWNLOADED!!")
    decorationPrints()

if __name__ == '__main__':
    main()