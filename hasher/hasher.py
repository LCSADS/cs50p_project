from passlib.hash import pbkdf2_sha256
import re
# generate hash
def hasher(password):
    hash = pbkdf2_sha256.hash(password)
    return hash
# check password
def verify_password(password, hash):
    verification = pbkdf2_sha256.verify(password,hash)
    return verification
# password policy
def password_policy(password):
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s]).{8,16}$"
    chosen_password = password
    if re.search(password_pattern,chosen_password):
        return True
    else:
        return False