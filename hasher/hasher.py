from passlib.hash import pbkdf2_sha256
# generate hash
def hasher(password):
    hash = pbkdf2_sha256.hash(password)
    return hash
# check password
def verify_password(password, hash):
    verification = pbkdf2_sha256.verify(password,hash)
    return verification
# password policy
