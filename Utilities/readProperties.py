import configparser

config=configparser.RawConfigParser()
config.read(".\\Resources\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getPageTile():
        url = config.get('common info', 'pageTitle')
        return url