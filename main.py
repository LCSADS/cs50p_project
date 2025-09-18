from hasher import hasher, verify_password,password_policy

password = input("What's your password?")
hash = hasher(password)

print(hasher(password))

print("verifying password..")

print(verify_password(password,hash))

if password_policy(password):
    print("Strong password")
else:
    print("Weak password.")