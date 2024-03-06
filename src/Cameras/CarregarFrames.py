from src.Cameras.ControleFluxo import ControleFluxo
from PyQt6 import QtGui
from threading import Thread
from datetime import datetime
import copy
import cv2

class CarregarFrames:
    def __init__(self, parent):
        self.parent = parent
        self.controle_fluxo = ControleFluxo(self)
        self.json_dados_fila = {}
        self.parent.janelaConfig.btn_fila.clicked.connect(lambda : Thread(target=self.coletar_signal_add_dados_fila, daemon=True).start())

    def coletar_farmes(self, dados_cameras, signal):
        for index in dados_cameras:
            dados_keys, dados_values = list(index.keys()), list(index.values())
            thread = Thread(target=self.carregar_frames_buffer, daemon=True, args=(dados_keys[0], dados_values[0], dados_values[1], dados_values[2], dados_values[3], self.json_dados_fila, dados_values[4], signal))
            thread.start()

    def carregar_frames_buffer(self, cam, cap, arena, modalidade, resolucao, dados_video, dados_links, signal):
        while True:
            if isinstance(cap, cv2.VideoCapture):
                if cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        if cam not in dados_video:
                            dados_video.update({cam : [{cam : [], "arena" : arena, "modalidade" : modalidade, "resolucao" : resolucao}]})
                        if len(dados_video[cam][0][cam]) < 550:
                            dados_video[cam][0][cam].append(frame)
                        elif len(dados_video[cam][0][cam]) == 550:
                            dados_video[cam][0][cam].pop(0)
                            dados_video[cam][0][cam].append(frame)
                    else:
                        try:
                            signal(f"Não foi possivel ler os dados dos frames da Câmera {cam.split('_')[1]}")
                            # cap.release()
                            # cap = cv2.VideoCapture(dados_links, cv2.CAP_FFMPEG)
                            dados_video[cam][0][cam].clear()
                        except:
                            pass
                else:
                    signal(f"Camera {cam.split('_')[1]} caiu")
                    # cap.release()
                    # cap = cv2.VideoCapture(dados_links, cv2.CAP_FFMPEG)
            else:
                signal(f"Câmera está desativada deis do inicio, Câmera {cam.split('_')[1]}")
                # cap = cv2.VideoCapture(dados_links, cv2.CAP_FFMPEG)

    def coletar_signal_add_dados_fila(self):
        name_cam = self.parent.janelaConfig.nome_cam.text()
        if name_cam in self.json_dados_fila:
            if len(self.json_dados_fila[name_cam][0][name_cam]) == 550:
                new_dados = copy.deepcopy(self.json_dados_fila[name_cam])
                new_dados[0].update({"date" : datetime.now().strftime("%Y%m%d_%H%M%S")})
                self.json_dados_fila[name_cam][0][name_cam].clear()
                self.controle_fluxo.adicionar_dados_fila_processamento(value=new_dados)

