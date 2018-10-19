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

def initialise_db():
    hids_database = mysql.connector.connect(user='root', password='Narnia0102',host='localhost',database='HIDS')
    return hids_database
    
#Adds file into the db for the first time. 
def track_file_initialisation(path_name, db):
    hash_object = hashlib.md5(path_name.encode())
    print(hash_object.hexdigest())
    hash_value = str(hash_object.hexdigest())
    print type(hash_value)
    query = "INSERT INTO file_checksum VALUES(hh,1);"
    print query
    insert_into_db(query , db)
    
def select_from_db(hids_database):
    cursor=hids_database.cursor()
    cursor.execute ("SELECT * FROM file_checksum;")
    row = cursor.fetchone()
    print "File:", row[0], "Checksum:", row[1]
    #cursor.close() - Was causing an error 
    
def insert_into_db(SQL_INSERT, hids_database):
    cursor=hids_database.cursor()
    cursor.execute("INSERT INTO file_checksum VALUES(3,1);")
    hids_database.commit()
    cursor.close()