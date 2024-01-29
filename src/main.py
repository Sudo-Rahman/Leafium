from time import sleep

from pymongo.errors import ConnectionFailure

from database import Database


def connection():
    host = "localhost"
    port = 27017
    database = "leafium"
    user = None
    password = None

    h = input("Apuyer sur entrer pour se connecter en local ou indiquer l'adresse du serveur\n")
    if h != "":
        host = h

    p = input("Apuyer sur entrer pour se connecter au port 27017 ou indiquer le port du serveur\n")
    if p != "":
        port = int(p)

    d = input(
        "Apuyer sur entrer pour se connecter à la base de données leafium ou indiquer le nom de la base de données\n")
    if d != "":
        database = d

    u = input("Apuyer sur entrer pour se connecter sans utilisateur ou indiquer le nom de l'utilisateur\n")
    if u != "":
        user = u
        password = input("Indiquer le mot de passe de l'utilisateur\n")

    db = Database(host, port, database, user, password)

    return db


if __name__ == '__main__':
    try:
        db = connection()
        sleep(1)
    except Exception as e:
        print("Server not available")
        exit(1)
    db.populate(10, 100)
