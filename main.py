from src.mediaforge.downloader import MediaDowloader

def main():
    url = input("Digite o link da sua URL: ")

    downloader = MediaDowloader()   
    downloader.download_audio(url)

    print("\nDownload completo!")

if __name__ == "__main__":
    main()