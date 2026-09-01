from src.mediaforge.downloader import MediaDowloader

class MediaForgeCLI:

    def __init__(self):
        self.downloader = MediaDowloader()

    def show_menu(self):
        print("\n=== MediaForge CLI ===")
        print("1. Baixar vídeo")
        print("2. Baixar áudio")
        print("3. Sair")

    def run(self):
        while True:
            self.show_menu()

            option = input("Escolha uma opção: ")

            match option:
                case "1":
                    self.download_video()
                case "2":
                    self.download_audio()
                case "3":
                    print("Encerrando o MediaForge CLI. Até logo!")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def download_video(self):
        url = input("Digite o link do vídeo: ")

        try:
            self.downloader.download_video(url)
            print("Download do vídeo concluído!")
        except Exception as error:
            print(f"Erro ao baixar o vídeo: {error}")

    def download_audio(self):
        url = input("Digite o link do áudio: ")

        try:
            self.downloader.download_audio(url)
            print("Download do áudio concluído!")
        except Exception as error:
            print(f"Erro ao baixar o áudio: {error}")