import subprocess
import os
import random
import asyncio

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class AudioVideoFFMPEG:
    def __init__(self):
        self.path = self.Path()
        self.lista_videos = []
        self.lista_audio = []

    async def adicionar_audio_all_videos(self):
        self.lista_videos = os.listdir(self.path.video_path)
        self.lista_audio = os.listdir(self.path.audio_path)
        if self.lista_videos and self.lista_audio:
            for video in self.lista_videos:
                audio = random.choice(self.lista_audio)
                print(audio)
                await self.adicionar_audio_video(video, audio)

    async def adicionar_audio_video(self, video, audio):
        file_name = f'{video[:video.find('.')]}_com_audio.mp4'
        file_path = os.path.join(self.path.saida_path, file_name)
        
        ffmpeg_command = [
            "ffmpeg",
            "-i", os.path.join(self.path.video_path, video),
            "-i", os.path.join(self.path.audio_path, audio),
            "-c:v", "copy",
            "-c:a", "aac",
            "-strict", "experimental",
            file_path
        ]

        try:
            subprocess.run(ffmpeg_command)
        except Exception as e:
            print(f'Erro ao tentar adicionar audio no vídeo. Motivo: {e}')


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

        self.audio_video = AudioVideoFFMPEG()
        self.button.clicked.connect(lambda: asyncio.run(self.audio_video.adicionar_audio_all_videos()))
        

if __name__ == '__main__':
    import sys
        
    app = QApplication(sys.argv)
    a = main()
    a.show()
    sys.exit(app.exec())


