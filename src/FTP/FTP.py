from ftplib import FTP
import json
import os

class FTPUploader:
    LINK_CONFIG = os.getcwd() + '\\src\\ArquivosConfiguracoes\\FTPConfig\\ftp.json'
    def __init__(self):
        self.pegar_dados_ftp_json()

    def pegar_dados_ftp_json(self):
        with open(FTPUploader.LINK_CONFIG) as f:
            ftp_config = json.loads(f.read())
            self.host = ftp_config["host"]
            self.username = ftp_config["username"]
            self.password = ftp_config["password"]
            self.diretorio_local = ftp_config["diretorio_local"]
            self.diretorio_remoto = ftp_config["diretorio_remoto"]

    def upload_video(self, name_video):
        try:
            with open(self.diretorio_local + name_video, 'rb') as file:
                ftp = FTP(self.host)
                ftp.login(user=self.username, passwd=self.password)
                ftp.cwd(self.diretorio_remoto)
                ftp.storbinary('STOR ' + name_video, file)
                ftp.quit()
        except Exception as e:
            print("Ocorreu um erro ao enviar o arquivo:", e)
