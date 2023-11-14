from enum import Enum
import yaml

class Config:
    os_type = ''
    email_port = 587
    email_server = ''
    email_sender = ''
    email_password = ''
    email_reciever = ''
    vote_urls = []
    minecraft_username = ''
    browser = ''

    def __init__(self, path_to_yaml):
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            self.os_type = config['os_type']
            self.email_sender = config['email_sender']
            self.email_password = config['email_password']
            self.email_reciever = config['email_reciever']
            for url in config['vote_urls']:
                self.vote_urls.append(url)
            self.minecraft_username = config['minecraft_username']
            self.browser = config['browser']

            # Set email server using the domain at the end
            if 'gmail' in self.email_sender:
                self.email_server = EmailServer.GMAIL
            elif 'yahoo' in self.email_sender:
                self.email_server = EmailServer.YAHOO
            elif 'outlook' in self.email_sender:
                self.email_server = EmailServer.OUTLOOK
            else:
                raise Exception('Email server not supported')


class OS(Enum):
    WINDOWS = 'windows'
    LINUX = 'linux'
    MAC = 'macOS'

    def __str__(self):
        return self.name
    
class EmailServer(Enum):
    GMAIL = 'smtp.gmail.com'
    YAHOO = 'smtp.mail.yahoo.com'
    OUTLOOK = 'smtp-mail.outlook.com'
