<<<<<<< HEAD
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import asyncio
import random

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


def tempo_execucao(funcao):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        tempo_total = fim - inicio
        print(f"A função {funcao.__name__} levou {tempo_total:.4f} segundos para ser executada.")
        return resultado
    return wrapper
=======
import cv2
from moviepy.editor import VideoFileClip
import os
>>>>>>> fd0780d659e4767d8e52230c1201fd23c8a8d115


class AudioVideo:
    def __init__(self):
<<<<<<< HEAD
        self.path = self.Path()
        self.lista_videos = []
        self.lista_audio = []

    async def adicionar_audio_all_videos(self):
        self.lista_videos = os.listdir(self.path.video_path)
        self.lista_audio = os.listdir(self.path.audio_path)

        if len(self.lista_videos) and len(self.lista_audio):
            for video in self.lista_videos:
                audio = random.choice(self.lista_audio)
                await self.adicionar_audio(video, audio)

    async def adicionar_audio(self, video:str, audio:str, in_time_audio:int=0):
        try:
            video_clip = VideoFileClip(os.path.join(self.path.video_path, video))
            audio_clip = AudioFileClip(os.path.join(self.path.audio_path, audio)).subclip(in_time_audio, video_clip.duration + in_time_audio)
            saida = video_clip.set_audio(audio_clip) 
           
            file_name = f'{video[:video.find('.')]}_com_audio.mp4'
            file_path = os.path.join(self.path.saida_path, file_name) 
            saida.write_videofile(file_path, codec='libx264', audio_codec='aac', temp_audiofile='tem-audio.m4a', remove_temp=True)  # Criar arquivo final
            
            os.system('cls')
        
        except OSError as e:
            print(f"Erro no caminho informado: {e}")
        
        except Exception as e:
            print(f"Erro ao adicionar o Audio no Vídeo. Motivo: {e}")


    class Path: 
        def __init__(self):
            self.SOFTWARE_PATH = os.getcwd()
            self.video_path = os.path.join(self.SOFTWARE_PATH, 'media', 'videos')
            self.audio_path = os.path.join(self.SOFTWARE_PATH, 'media', 'audios')
            self.saida_path = os.path.join(self.SOFTWARE_PATH, 'media', 'videos_prontos')   


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(600)
        self.setMinimumWidth(400)
        self.layout_1 = QHBoxLayout(self)
        self.layout_1.setContentsMargins(10, 10, 10, 10)
        self.button = QPushButton(self)
        self.button.setText("Coletar Audio")
        self.layout_1.addWidget(self.button) 

        self.audio_video = AudioVideo()
        self.button.clicked.connect(lambda: asyncio.run(self.audio_video.adicionar_audio_all_videos()))
        


if __name__ == '__main__':
    import sys
        
    app = QApplication(sys.argv)
    a = main()
    a.show()
    sys.exit(app.exec())

=======
        self.software_path = os.getcwd()
        self.video_path = self.software_path + 'media\\videos\\'
        self.audio_path = self.software_path + 'media\\audios\\aud_1.mp3'
        self.saida_path = self.software_path + 'media\\videos_prontos\\'
     
    def addAudio(self):
        video = VideoFileClip(self.video_path) #Carregar vídeo
        audio_clip = VideoFileClip(self.audio_path).subclip(0, video.duration) #Carregar audio
        saida = video.set_audio(audio_clip) #Adicionar audio ao vídeo
        video.write_videofile(self.saida_path, codec='libx264', audio_codec='aac', temp_audiofile='tem-audio.m4a', remove_temp=True) #Criar arquivo final
     
     
     
      
>>>>>>> fd0780d659e4767d8e52230c1201fd23c8a8d115
