# A simple logger class that I can then email to myself, instead of saving it to a file
import email
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Logger:
    logs = []
    def __init__(self, sender: str, sender_pass: str, reciever: str):
        self.sender = sender
        self.sender_password = sender_pass
        self.reciever = reciever
        self.logs = []

    def log(self, message: str):
        self.logs.append(message + '\n')

    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.sender_password)
        # New MIME object
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.reciever
        msg['Subject'] = f'AutoVote logs from {datetime.datetime.now()}'
        msg.attach(MIMEText(''.join(self.logs), 'plain'))
        server.send_message(msg)
        server.quit()