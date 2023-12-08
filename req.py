import mysql.connector
import hashed
from base64 import b64encode

# CREATE TABLE accounts(idUser INT NOT NULL AUTO_INCREMENT, username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL,sessionToken VARCHAR(100), salt VARCHAR(100) NOT NULL, Primary key(idUser)) ;

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="NDI"
)

mycursor = mydb.cursor()

def check_user(user,passwd):

    mycursor.execute("SELECT password FROM accounts WHERE username = %s ", (user,))
    hashed_password = mycursor.fetchone()
    r = hashed.verify_password(passwd, hashed_password)
    if r :
        mycursor.execute("SELECT idUser FROM accounts WHERE username = %s AND password = %s ", (user,hashed_password[0]))
        return mycursor.fetchone()[0]
    return None

def create_user(user,passwd):
    """hashed_passwd[0] = hashed password"""
    hashed_passwd = hashed.hash_password(passwd)

    mycursor.execute("INSERT INTO accounts (username,password) VALUES (%s,%s)",(user,hashed_passwd))
    mydb.commit()

print(check_user("admin","admin"))
#create_user("admin","admin")