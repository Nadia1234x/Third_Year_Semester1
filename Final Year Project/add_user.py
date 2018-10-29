import database 

admin_user = int(raw_input('Are you the admin? Enter 1 for Yes, 0 for No'))
if(admin_user == 1):
    admin_user = raw_input('Please enter the admin username: ')
    admin_pass = raw_input('Please enter the admin password: ')
    new_user = raw_input('Please enter the new users username: ')
    new_user_pass = raw_input('Please enter the new users password: ')
    
else: 
    "Please contact the admin at nadianoormohamed96@gmail.com to request account, specify the username and password in the email. Please make sure to change the password after the account has been created."
def add_user(new_user, new_user_pass, admin_username, admin_password): 
    query = "CREATE USER '" + new_user + "'@'localhost' IDENTIFIED BY '" + new_user_pass + "';"
    print query
    db = database.initialise_db(admin_username, admin_password)
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    query = "USE HIDS;"
    cursor.execute(query)
    db.commit()
    query = "CREATE TABLE " + new_user + "_file_checksum( ID int, checksum VARCHAR(200));"
    cursor.execute(query)
    db.commit()
    query = "GRANT ALL ON HIDS." + new_user + "_file_checksum" + "TO '" + new_user + "'@'localhost';"
    print query
    
add_user(new_user, new_user_pass, admin_user, admin_pass)  