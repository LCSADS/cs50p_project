from hasher import hasher, verify_password

password = input("What's your password?")
hash = hasher(password)

print(hasher(password))

print("verifying password..")

print(verify_password(password,hash))