from storage import find_user
from hasher import verify_password

def login(username,password):

    user = find_user(username)
    if user is None:
        print(f"The username '{username}' was not found.")
        return None

    if verify_password(password,user._password_hash):
        print(f"{username} authenticated successfully.")
        return user
    else:
        print(f"The typed password doesn't correspond with the user {username}")
        return None