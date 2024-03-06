from moviepy.editor import AudioFileClip
import os


class CortarAudio:
    def __init__(self):
        self.caminho = os.getcwd()
        self.input_audio = os.path.join(self.caminho, "media", "audios", "linkin-park_whatisdone.mp3")
        self.output_audio = os.path.join(self.caminho, "media", "audios", "linkin-park_whatisdone_cortado.mp3")
    
    def cortar_audio(self, start_time, end_time):
        audio_clip = AudioFileClip(self.input_audio)
        audio_cortado = audio_clip.subclip(start_time, end_time)
        audio_cortado.write_audiofile(self.output_audio)


if __name__ == '__main__':
    cortar = CortarAudio()
    cortar.cortar_audio(start_time=40, end_time=62)