import yt_dlp

class MediaDownloader:

    def __init__(self, output_path="downloads"):
        self.output_path = output_path

    def download_video(self, url):
        options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{self.output_path}/Video/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def download_audio(self, url):
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"{self.output_path}/Audio/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def download_playlist(self, url):
        options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{self.output_path}/Playlist/%(playlist_title)s/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "ignoreerrors": True,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)

            total = len(info.get("entries", []))
            downloaded = 0
            ignored = 0

            for entry in info.get("entries", []):
                if entry is None:
                    ignored += 1
                    continue

                try:
                    ydl.download([entry["webpage_url"]])
                    downloaded += 1
                except Exception:
                    ignored += 1

            return total, downloaded, ignored