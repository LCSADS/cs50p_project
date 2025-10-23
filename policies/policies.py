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
    if len(password) < 8 or len(password) > 16:
        print("Lenght between 8 and 16 characters.")

def username_policy(username:str):
    username_pattern = re.compile(r'^(?=.{5,20}$)(?!.*[._-]{2})(?!.*(.)\1\1)[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9]$')
    chosen_username = username
    if re.search(username_pattern,chosen_username):
        return True
    else:
        return False
    
def invalid_username_feedback(username:str):
    
    # check username lenght
    if len(username) < 5 or len(username) > 20:
        print(f"In between 5 and 20 characters.")
    
    # check if the username starts with a letter
    if not re.match(r"^[A-Za-z]",username):
        print(f"The starting character must be a letter")
    
    # check if the last character is alphanumeric
    if not re.search(r"[A-Za-z0-9]$", username):
        print(f"The last character should be a letter or a number.")

    # check if the username has any forbidden characters like a $
    if re.search(r"[^A-Za-z0-9._-]",username):
        print(f"Only letters, digits, dots, underscores and hyphens are allowed")

    # check if there's adjacent separators like ---- or __ or ._.
    if re.search(r"[._-]{2}",username):
        print(f"No two separators in a row. I.E : ._ or .. or __")
   
    # check if there's 3 characters repeating in a row.
    if re.search(r"(.)\1\1",username):
        print(f"No characters can appear 3 times in a row.")


