from factory import create_user
from hasher import hasher, verify_password
from entities import User
from policies import username_policy, security_feedback, password_policy
import re

password_input = input("type password")

passhash = hasher(password_input)
print(f" Hash : {passhash}")

print("pass check")

verification = verify_password(password_input,passhash)

print(f" Return value : {verification}")

if verification:
    print("correct output so far")
else:
    print("oops")


valid_username = "alice.santos"
valid_password = "Str0ngP@ss!"

new_user_sucess = create_user(valid_username,valid_password)

if new_user_sucess:
    print("sucess!")
    print(f"\n deu certo. objeto criado : {new_user_sucess.user_info()}")
    print(f" Hash guardado - {new_user_sucess._password_hash[:40]}")

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


