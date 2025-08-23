from pytube import YouTube

try:
    #Here we gonna paste the actual URL
    url = input("Enter URL: ")
    yt = YouTube(url)
    
    #Information about video 
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    #Here we are gonna get the Highest possible resolution of our video
    res = yt.streams.get_highest_resolution()

    #Downloading video
    res.download('E:\\YT_videos')


    print("Download complete!")
except Exception as e:
    print(f"Something went wrong with your download sir. Error: {e}")
