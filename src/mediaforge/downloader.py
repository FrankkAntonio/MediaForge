import yt_dlp

class MediaDowloader:

    def __init__(self, output_path="downloads"):
        self.output_path = output_path

    def download_video(self, url):
        options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
            



