import yt_dlp
import tkinter as tk

def download():
    url = area.get()
    save_location = area2.get()
    try:
        ydl_opts = {
        'outtmpl' : rf'{save_location}\%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        label = tk.Label(root, text=f"Video downloaded. Location: {save_location}")
        label.pack(pady=5)
    except Exception as e:
        label = tk.Label(root, text=f"An error has occured. ERROR: {e}")
        label.pack(pady=5)
        try:
            label = tk.Label(root, text="Possibly ffmpeg not detected. Video will be downloaded with worse quality.")
            label.pack(pady=5)
            ydl_opts = {
                'outtmpl' : rf'{save_location}\%(title)s.%(ext)s',
                'format' : 'best', # single stream 
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except Exception as e:
            print(f"Sorry sir, your video cannot be downloaded properly. ERROR: {e}")
    
#GUI Initialization 
root = tk.Tk()
root.title("YT Video downloader by HuXib")
root.geometry("500x200")

#Basic label for my GUI
label = tk.Label(root, text="Paste the YT video link to area below.")
label.pack(pady=5)

#Area to type URL 
area = tk.Entry(root,width=50)
area.pack(pady=5)

#Label for loaction
label = tk.Label(root, text="Paste location where file will be saved and click download button.")
label.pack(pady=5)

#Area to select where file will be saved
area2 = tk.Entry(root, width=50)
area2.pack(pady=5)

#Button to download 
button = tk.Button(root, text="Download", command=download, width=15)
button.pack(pady=5)


root.mainloop()


