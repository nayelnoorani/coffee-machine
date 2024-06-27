from users import users
import getpass

def user_exists(username):
    return username in users
    
def check_password(username, password):
    if user_exists(username):
        return users[username]['password'] == password 

def authenticate_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return (user_exists(username) 
        and check_password(username, password)
        and users[username]['role'] == 'admin')
