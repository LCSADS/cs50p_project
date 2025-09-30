import re

# password policy
def password_policy(password):
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s]).{8,16}$"
    chosen_password = password
    if re.search(password_pattern,chosen_password):
        return True
    else:
        return False
    
def security_feedback(password):
    print("Your password is not strong enough")
    print("Please make sure your password has the following :")
    if not re.search(r"[A-Z]",password):
        print("At least one capital letter.")
    if not re.search(r"[a-z]",password):
        print("At least one lower letter.")
    if not re.search(r"[0-9]",password):
        print("At least one number")
    if not re.search(r"[^A-Za-z\d\s]",password):
        print("At least one special character.")

def username_policy(username:str):
    username_pattern = r"^[a-zA-Z0-9._-]{5,20}"
    chosen_username = username
    if re.search(username_pattern,chosen_username):
        return True
    else:
        return False