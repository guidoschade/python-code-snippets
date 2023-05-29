# pip3 install pytube
from pytube import YouTube

# main function
def main():
    url = input("Enter the YouTube video URL: ")
    DownloadVideo(url)


# downloading
def DownloadVideo(url):
    # creating new handle
    handle = YouTube(url)

    # selecting the best resolution from available streams
    handle = handle.streams.get_highest_resolution()
    try:
        # try to download the file
        handle.download()
    except:
        print("Error, download failed")
    print("Download completed successfully")


# run main if called directly
if __name__ == "__main__":
    main()

# example: https://www.youtube.com/watch?v=dQw4w9WgXcQ