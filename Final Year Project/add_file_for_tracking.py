import database
import argon2
import hash 

#This file will be executed when the user clicks on the track new file button.
 
track_file = int(raw_input("do you want to to track a file? Yes = 1, No = 0: "))

#Need to derive the key used to create file checksum



if(track_file == 1):
    
    username = raw_input("Please enter your username: ")
    password = raw_input("Please enter you password: ")
    path_name = raw_input("Please enter the absolute pathname of the file")
     
    secret_key = hash.derive_secret_key(password)
    path_hash = hash.generate_filePathName_checksum(path_name)
    file_hash = hash.generate_file_checksum(path_name, secret_key)
    
    db = database.initialise_db(username, password)
    database.track_new_file_initialisation(path_hash, file_hash, db);
else: 
    quit()