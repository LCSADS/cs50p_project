from factory import create_user
from hasher import hasher, verify_password
from entities import User
from policies import username_policy, security_feedback, password_policy
from user_input import confirm, get_valid_password, get_valid_username
import re

password_input = get_valid_password()

passhash = hasher(password_input)
print(f" Hash : {passhash}")

print("password checked")

username_input = get_valid_username()

verification = verify_password(password_input,passhash)

print(f" Return value from password verification : {verification}")

if verification:
    print("correct output so far")
else:
    print("oops")

new_user = create_user(username_input,password_input)

if new_user:
    print("sucesso!")
    print(f"\n deu certo. objeto criado : {new_user.user_info()}")
    print(f" Hash guardado - {new_user._password_hash[:40]}")

else: 
    print("num criou")


print("cenario de falha")
invalid_username = "bob"
invalid_password = "bob"
new_user_failure = create_user(invalid_username,invalid_password)

if new_user_failure is None:
    
    print(f"sucesso nada foi criado.")


else:
    print("ooops")


