import mysql.connector

# CREATE TABLE accounts(idUser INT NOT NULL AUTO_INCREMENT, username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL,sessionToken VARCHAR(100), Primary key(idUser)) ;

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="NDI"
)

mycursor = mydb.cursor()

def check_user(user,passwd):
    mycursor.execute("SELECT idUser FROM accounts WHERE username = %s AND password = %s ", (user,passwd))
    return mycursor.fetchone()

print(check_user("admin","admin"))
   