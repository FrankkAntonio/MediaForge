import yt_dlp

class MediaDowloader:

    def __init__(self, output_path="downloads"):
        self.output_path = output_path

    def download_video(self, url):
        options = {
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
            



