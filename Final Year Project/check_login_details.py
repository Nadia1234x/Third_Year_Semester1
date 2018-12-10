import database
import unicodedata

def validate_credentials(username, input_password):
    
    query = "SELECT password FROM login WHERE username = '" + username + "';"
    db = database.initialise_db("root", "Narnia0102")
    result = database.query_select(query, db)

    if(result[0][0] == input_password):
        print "You are logged in"
    
    