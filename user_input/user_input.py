import sys
import policies
import storage

def confirm(message : str):
    while True:
        user_answer = input(f"{message} \n Type [Y] for yes and [N] for no. Press Enter to exit.").strip().upper()

        if not user_answer:
            sys.exit("Exiting the program.")
        elif user_answer in "YN":
            if user_answer == "Y":
                return True
            elif user_answer == "N":
                return False
        else:
            print("Invalid answer.")


def get_valid_username():
    while True:
        username = input("Please choose your username: ").strip()

        if not policies.username_policy(username):
            print(f"{username} is not a valid username.\n Please make sure your username contains no blank spaces and is between 5 and 20 characters in length")
            continue
        if storage.check_username_existence(username):
            print(f"The username: '{username}' is already in use. Please choose another one")
            continue
        if confirm(f"You chose {username} as your username. Continue?"):
            return username
        
def get_valid_password():
    while True:
        password = input("Type your password: ").strip()
        
        if not policies.password_policy(password):
            policies.security_feedback(password)
            continue

        confirm_password = input("Please type your password again to confirm the password.")
        if confirm_password != password:
            print("Didn't match.")
            continue
        
        return password
    

