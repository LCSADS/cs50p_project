from entities import User
from hasher import hasher
from policies import password_policy, username_policy
def create_user(username: str, password : str):
    if not username_policy(username):
        print(f"Failed to create user : {username} is invalid.")
        return None
    if not password_policy(password):
        print(f"Failed to create user {username}:\n Password didn't fulfill the requirments")
        return None
    
    password_hash = hasher(password)

    new_user = User(
        username = username,
        password_hash = password_hash
    )

    print(f" User {username} created sucessfully")

    return new_user
    
