import database 

admin_user = int(raw_input('Are you the admin? Enter 1 for Yes, 0 for No'))
if(admin_user == 0):
    print "Please contact the admin to add the user at nadianoormohamed96@gmail.complex"
else: 
    username = raw_input('Please enter the username: ')
    password = raw_input('Please enter the password: ')
    
    new_user = raw_input('Please enter the username of the new user: ')
    new_user_pass = raw_input('Please enter the password of the new user: ')
    
def add_user(): 
    database = database.initialise_db(username, password)
    query = ''
    
    
    
    