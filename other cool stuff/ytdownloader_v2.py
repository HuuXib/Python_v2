import yt_dlp

url = input("Enter URL: ")

try:
    ydl_opts = {
    'outtmpl' : r'E:\YT_videos\%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except Exception as e:
    print(f"An error has occured. ERROR: {e}")
    try:
        print("Possibly ffmpeg not detected. Video will be downlaoded with worse quality.")
        ydl_opts = {
            'outtmpl' : r'E:\YT_videos\%(title)s.%(ext)s',
            'format' : 'best', # single stream 
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(f"Sorry sir, your video cannot be downloaded properly. ERROR: {e}")
    
