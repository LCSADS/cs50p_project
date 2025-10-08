from factory import create_user
from auth import login
from storage import save_user, find_user
from policies import security_feedback 
from user_input import get_valid_password, get_valid_username
from hasher import verify_password

print("\nconceito")
print("\nCriação de usuário")
username = get_valid_username()
password = get_valid_password()

new_user = create_user(username, password)

if new_user:
    save_user(new_user)
    print("\nsucesso")
else:
    print("\nerro")

login_success = login(username, password)

if login_success:
    print(f"\nlogin bem sucedido {login_success.username} recuperado do json")
else:
    print("\ndeu erro no json")
print("\ntesting failure to login with wrong password")
## failure test
wrong_password = "whatever"
invalid_password_login = login(username,wrong_password)
if invalid_password_login is None:
    print(f"\nSucessfully blocked login with wrong password")
else:
    print(f"\nfailure, login was successfull even with the wrong password")


print("\ntesting failure to login with invalid username")

invalid_user_login = login("whatever",password)
if invalid_user_login is None:
    print(f"\nSucessfully blocked login with wrong username")
else:
    print(f"failure. login was successful with a invalid username")