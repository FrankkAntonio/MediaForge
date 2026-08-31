import yt_dlp

class mediaDowloader:

    def __init__(self, output_path="downloads"):
        self.output_path = output_path

    def download_video(self, url):
        options = {
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
            



