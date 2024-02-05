from time import sleep

from pymongo.errors import ConnectionFailure

from database import Database


def connection():
    host = "localhost"
    port = 27017
    database = "leafium"
    user = None
    password = None

    h = input("Appuyez sur Entrée pour vous connecter en \033[92mlocal\033[97m ou indiquez l'adresse du serveur\n")
    if h != "":
        host = h

    p = input("Apuyer sur entrer pour se connecter au port \033[92m27017\033[97m ou indiquer le port du serveur\n")
    if p != "":
        port = int(p)

    d = input(
        "Apuyer sur entrer pour se connecter à la base de données \033[92mleafium\033[97m ou indiquer le nom de la base de données\n")
    if d != "":
        database = d

    u = input(
        "Apuyer sur entrer pour se connecter \033[92msans utilisateur\033[97m ou indiquer le nom de l'utilisateur\n")
    if u != "":
        user = u
        password = input("Indiquer le \033[92mmot de passe\033[97m de l'utilisateur\n")

    db = Database(host, port, database, user, password)

    return db


if __name__ == '__main__':
    try:
        db = connection()
        sleep(1)
    except Exception as e:
        print("\033[91mServeur non disponible\033[97m ->", e)
        exit(1)
    print("\033Connexion réussie\033[97m")
    db.populate(100)
    # db.get_average_rating_by_movie(5)
    # db.get_movie_by_category("Action")
    # db.get_movie_by_director("Steven Spielberg")
    # db.get_top_movies_by_tickets_sold(5)
