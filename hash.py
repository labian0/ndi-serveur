import hashlib, os


#taille sha256: 256 bits, soit 32 octets 
HASH = hashlib.new('sha256')


def hash_password(password: str):
    #Génération aléatoire d'un salt
    salt = os.urandom(32)

    combined = bytes(bytes(password) + salt)
    hashed_password = HASH.update(combined)
    hashed_password.digest()


    return salt, hashed_password    #on renvoie le hash du password combiné avec le salt ainsi que le salt


def verify_password(password: str, hashed_password, salt_from_db):
    password = password.encode('utf-8')

    combined = password + salt_from_db
    test_hashed_password = HASH.update(combined).hexdigest()

    if test_hashed_password == hash_password:
        print ("Mot de passe correct")

    else:
        print ("Incorrect")
print(hash_password("zouzou"))