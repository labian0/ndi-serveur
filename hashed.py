import hashlib

def hash_password(password):
    password_bytes = password.encode('utf-8')

    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

def verify_password(password, hashed_password):
    password_bytes = bytes(password, "utf-8")
    new_hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return new_hashed_password == hashed_password[0]   #on renvoi 1 si les passwords sont égaux sinon 0