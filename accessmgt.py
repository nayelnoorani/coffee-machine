from users import users
import getpass

def user_exists(username):
    if username in users:
        return True
    else:
        return False
    
def check_password(username, password):
    if user_exists(username):
        if users[username]['password'] == password:
            return True
        else:
            return False
    else:
        return False

def authenticate_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if (user_exists(username) 
        and check_password(username, password)
        and users[username]['role'] == 'admin'):
        return True
    else:
        return False