from PyQt6 import QtCore, QtWidgets, QtGui
import os
import json
import cv2

class ListaCameras(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.lista_cameras = QtWidgets.QListWidget()


class Cameras(ListaCameras):
    link_cameras = os.getcwd() + '\\src\\ArquivosConfiguracoes\\CamerasConfig\\cameras.json'
    def __init__(self):
        super().__init__()
        self.__dados_cameras = []
        self.__dados_links = []

    @property
    def dados_cameras(self):
        return self.__dados_cameras

    @dados_cameras.setter
    def dados_cameras(self, value):
        self.__dados_cameras = value
        return self.__dados_cameras

    @property
    def dados_links(self):
        return self.__dados_links

    @dados_links.setter
    def dados_links(self, value):
        self.__dados_links = value
        return self.__dados_links

    def buscar_dados_cameras(self):
        with open(Cameras.link_cameras, 'r', encoding='utf-8') as f:
            res = json.loads(f.read())
        self.__dados_links = res

    def montar_item(self, keys, status):
        text = keys[0].split('_')[1]
        if status:
            item = QtWidgets.QListWidgetItem()
            item.setText(f'Câmera {text}')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(':icons/cam_on.svg'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            item.setIcon(icon)
            self.lista_cameras.addItem(item)
        else:
            item = QtWidgets.QListWidgetItem()
            item.setText(f'Câmera {text}')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(':icons/cam_off.svg'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            item.setIcon(icon)
            self.lista_cameras.addItem(item)

    def montar_dados_json(self, index):
        coletar_keys = list(index.keys())
        status_cam = cv2.VideoCapture(index[coletar_keys[0]], cv2.CAP_FFMPEG)
        try:
            if not status_cam.isOpened():
                raise IOError(f"Não foi possivel conectar a {index[coletar_keys[0]]}, arena {index[coletar_keys[1]]}, modalidade {index[coletar_keys[2]]}.")
            else:
                self.montar_item(coletar_keys, status=True)
                return {coletar_keys[0] : status_cam, coletar_keys[1] : index[coletar_keys[1]], coletar_keys[2] : index[coletar_keys[2]], coletar_keys[3] : index[coletar_keys[3]], "link" : index[coletar_keys[0]]}
        except:
            self.montar_item(coletar_keys, status=False)
            return {coletar_keys[0] : f"Erro na camera {coletar_keys[0]}", coletar_keys[1] : index[coletar_keys[1]], coletar_keys[2] : index[coletar_keys[2]], coletar_keys[3] : index[coletar_keys[3]], "link" : index[coletar_keys[0]]}

    def verificar_conexao_cameras(self):
        self.buscar_dados_cameras()
        res = list(map(self.montar_dados_json, self.dados_links))
        self.__dados_cameras = res
        return self.__dados_cameras

