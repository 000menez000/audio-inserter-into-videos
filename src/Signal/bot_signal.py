from telebot import TeleBot
import os
import json


class BotSignalTelegram:
    def __init__(self):
        self.config = BotSignalTelegram.ConfigBOT()
        self.BOT = TeleBot(self.config.token)

    def enviarMensagem(self, mensagem:str):  
            for user in list(self.config.users.keys()):
                try:
                    self.BOT.send_message(chat_id=self.config.users[user], text=mensagem)
                except Exception as e:
                    print(f'ERRO! Não foi possível enviar mensagem de notificação para o {user}. MOTIVO:', e)


    class ConfigBOT:
        pathJsonInfoBot = os.getcwd() + "\\src\\ArquivosConfiguracoes\\SignalConfig\\bot.json" 
        def __init__(self):
            self.__dados = {}
            self.__token = ''
            self.__users = {}
            self.getInfoBot()

        @property
        def dados(self):
            return self.__dados
        
        @dados.setter
        def dados(self, value):
            self.__dados = value if isinstance(value, dict) else self.__dados
            return self.dados
        
        @property
        def token(self):
            return self.__token
        
        @token.setter
        def token(self, value):
            self.__token = value if isinstance(value, str) else self.__token
            return self.__token
        
        @property
        def users(self):
            return self.__users
        
        @users.setter
        def users(self, value):
            self.__users = value if isinstance(value, dict) else self.__users
            return self.__users            
            
        def getInfoBot(self):
            with open(BotSignalTelegram.ConfigBOT.pathJsonInfoBot, 'r', encoding='utf-8') as r:
                res = json.loads(r.read())
            self.dados = res
            self.token = self.dados['token']
            self.users = self.dados['users_id']        
