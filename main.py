from src.mediaforge.downloader import mediaDowloader

def main():
    url = input("Digite o link da sua URL: ")

    downloader = mediaDowloader()
    downloader.download_video(url)

    print("\nDownload completo!")

if __name__ == "__main__":
    main()