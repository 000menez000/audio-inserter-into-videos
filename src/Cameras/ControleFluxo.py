from src.FTP.FTP import FTPUploader
from PyQt6 import QtGui
from queue import Queue
from threading import Thread
import cv2
import time
import os

class ControleFluxo:
    VIODEO_SEM_TRATAMENTO = os.getcwd()+"\\src\\Video\\VideoSemTratamento\\"
    def __init__(self, parent):
        self.parent = parent
        self.ftp = FTPUploader()
        self.decoder = cv2.VideoWriter_fourcc(*'mp4v')
        self.fila_processamento = Queue(maxsize=5)
        Thread(target=self.consumir_dados_fila_processamento, daemon=True).start()

    def adicionar_dados_fila_processamento(self, value):
        self.fila_processamento.put(value)

    def cortando_video_on(self, value):
        for index in range(self.parent.parent.lista_cameras.count()):
            item = self.parent.parent.lista_cameras.item(index)
            item_text = item.text().split(' ')[1]
            if item_text == str(value):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(':/icons/cam_corte.svg'))
                item.setIcon(icon)

    def cortando_video_off(self, value):
        for index in range(self.parent.parent.lista_cameras.count()):
            item = self.parent.parent.lista_cameras.item(index)
            item_text = item.text().split(' ')[1]
            if item_text == str(value):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(':/icons/cam_on.svg'))
                item.setIcon(icon)

    def consumir_dados_fila_processamento(self):
        while True:
            time.sleep(0.1)
            for _ in range(self.fila_processamento.qsize()): 
                dados = self.fila_processamento.get()
                keys = list(dados[0].keys())
                name_video = f'{dados[0][keys[2]]}_{dados[0][keys[1]]}_{dados[0][keys[4]]}.mp4'
                width, height = int(dados[0][keys[3]].split('x')[0]), int(dados[0][keys[3]].split('x')[1])
                video = cv2.VideoWriter(ControleFluxo.VIODEO_SEM_TRATAMENTO+name_video, self.decoder, 25, (width, height))
                Thread(target=self.cortando_video_on(value=keys[0].split('_')[1]), daemon=True).start()
                for x in dados[0][keys[0]]:
                    video.write(x)
                video.release()
                Thread(target=self.cortando_video_off(value=keys[0].split('_')[1]), daemon=True).start()
                dados.clear()
                keys.clear()
                time.sleep(0.5)
                Thread(target=self.ftp.upload_video(name_video=name_video), daemon=True).start()

