import json
from pathlib import Path
from entities import User

json_path = Path("data/users.json")


def user_to_dict(user):
    return {
        "username": user.username,
        "password_hash": user._password_hash
    }

def dict_to_user(user_dictionary):
    return User (
        username = user_dictionary["username"],
        password_hash = user_dictionary["password_hash"]
    )

def load_users():
    if not json_path.exists():
        return []
    try:
        with open(json_path,'r') as file:
            data_list = json.load(file)

            user_objects_list = []
            for user_dict in data_list:
                user_object = dict_to_user(user_dict)
                user_objects_list.append(user_object)
            return user_objects_list
    except json.JSONDecodeError:
        return []
    

def save_user(new_user):
    users_list = load_users()   
    users_list.append(new_user)
    user_data_to_save = []
    for user in users_list:
        user_dictionary = user_to_dict(user)
        user_data_to_save.append(user_dictionary)
    with open(json_path,'w') as file:
# ident = 4 makes it look like python code idention, making it easier to read
        json.dump(user_data_to_save,file,indent=4)


def find_user(username):
    users_list = load_users()
    for user_object in users_list:
        if user_object.username == username:
            return user_object
    return None

def check_username_existence(username):
    user = find_user(username)
    if user is None:
        return False
    else:
        return True