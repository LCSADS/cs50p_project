from factory import create_user
from auth import login
from storage import save_user, find_user
from policies import security_feedback 
from user_input import get_valid_password, get_valid_username
from hasher import verify_password
import sys
def create_account():
    print(f"New account :")
    username = get_valid_username()
    password = get_valid_password()
    new_user = create_user(username, password)
    if new_user:
        save_user(new_user)
        print(f"\nAccount '{username}' created.")
def authentication():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    login_attempt = login(username,password)
    if login_attempt:
        print(f"Welcome {username}!")
        return True
    return False

def menu():
    while True:
        print("\nMenu\n")
        print("1 - Create new account")
        print("2 - Login")
        print("3 - Exit")
        choice = input("Type the option number to select: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            authentication()
        elif choice == '3':
            sys.exit("Bye!")
        else:
            print(f"Please select a valid option.")


def main():
    menu()


if __name__ == '__main__':
    main()