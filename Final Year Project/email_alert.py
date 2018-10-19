import os.path
import mysql.connector 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import schedule
import time
import hashlib
import sys
from subprocess import Popen, PIPE

def send_alert(line):
    fromaddr = "nadianoormohamed96@gmail.com"
    toaddr = "nadianoormohamed96@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = "nadianoormohamed96@gmail.com"
    msg['To'] = "nadianoormohamed96@gmail.com"
    msg['Subject'] = "Your file", line, "has been deleted"
    body = "Security alert: your file has been deleted"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    #server.starttls()
    server.login("nadianoormohamed96@gmail.com", "Narnia0102199604")

    text = msg.as_string()
    server.sendmail("nadianoormohamed96@gmail.com", "nadianoormohamed96@gmail.com", text)
    server.quit()