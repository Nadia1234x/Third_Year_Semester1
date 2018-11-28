import os.path
import mysql.connector
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from apscheduler.scheduler import Scheduler
import schedule
import time
import argon2
import hashlib
import sys
from subprocess import Popen, PIPE
import database
import email_alert
import check_fileExistence
import user_details
import hash

username = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")

def check_file_integrity():
    with open("tracked_file.txt") as file:
        for path in file:
            path = path.strip()
            compare_checksum(path)
         

def compare_checksum(path, username, password):
    secret_key = hash.derive_secret_key(password)
    path_hash = hash.generate_filePathName_checksum(path)
    new_file_checksum = hash.generate_file_checksum(path, secret_key)
    query = "SELECT checksum FROM file_checksum WHERE ID = '" + username + "_" + path_hash + "';"
    old_file_checksum = database.query_select(query)
   
    if(new_file_checksum == old_file_checksum):
        return True
    else:
        return False


check_file_integrity()

