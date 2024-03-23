import configparser
#This code is for reading configuration data from an INI file using Python's configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod

    def getuseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
