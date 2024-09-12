import pygame
from tkinter import Tk, filedialog
import sys

def selecionar_arquivo():
    root = Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo MP3",
        filetypes=[("Arquivo MP3", "*.mp3")]
    )
    return arquivo

# Inicializa o mixer do pygame
pygame.mixer.init()

# Abre o diálogo para o usuário selecionar o arquivo MP3
caminho_arquivo = selecionar_arquivo()

if caminho_arquivo:  # Verifica se um arquivo foi selecionado
    try:
        # Carrega o arquivo MP3
        pygame.mixer.music.load(caminho_arquivo)

        # Reproduz o áudio
        pygame.mixer.music.play()

        # Aguarda até a reprodução terminar
        try:
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except KeyboardInterrupt:
            print("Reprodução interrompida pelo usuário.")
            pygame.mixer.music.stop()
            sys.exit()
    except pygame.error as e:
        print(f"Erro ao reproduzir o áudio: {e}")
else:
    print("Nenhum arquivo selecionado.")