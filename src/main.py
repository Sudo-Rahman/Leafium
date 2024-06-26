from time import sleep
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from database import Database


def connection():
    """
    Connection à la base de données MongoDB en local ou sur le serveur de l'IEM
    :return:
    """
    host = "localhost"
    port = 27017
    database = "leafium"
    user = None
    password = None

    iem = input("Se connecter à \033[92ml'IEM ?\033[97m (y/n)\n")
    if iem == "y":
        user = input("Indiquer le \033[92mnom d'utilisateur\033[97m\n") or ""
        try:
            host = "mongo2.iem"
            return Database(host, port, user, user, user)
        except ConnectionFailure as e:
            print("\033[91mServeur non disponible\033[97m ->", e)
            exit(1)
    else:
        try:
            host = input(
                "Appuyez sur Entrée pour vous connecter en \033[92mlocal\033[97m ou indiquez l'adresse du serveur\n") or host
            port = input(
                "Apuyer sur Entrée pour se connecter au port \033[92m27017\033[97m ou indiquer le port du serveur\n") or port
            database = input(
                "Apuyer sur Entrée pour se connecter à la base de données \033[92mleafium\033[97m ou indiquer le nom de la base de données\n") or database
            user = input(
                "Apuyer sur Entrée pour se connecter \033[92msans utilisateur\033[97m ou indiquer le nom de l'utilisateur\n") or user
            if user:
                password = input("Indiquer le \033[92mmot de passe\033[97m de l'utilisateur\n")
            return Database(host, port, database, user, password)
        except ConnectionFailure as e:
            print("\033[91mServeur non disponible\033[97m ->", e)
            exit(1)


if __name__ == '__main__':
    try:
        # Connexion à la base de données
        db = connection()
        sleep(1)
        print("\033[92m*** Connexion réussie à", db.host, "sur le port", db.port, "en tant que", db.user, "***\033[97m")
        db.drop_collection()

        # Création de la collection
        db.populate(1000)

        # Exemple de requêtes
        db.get_average_rating_by_movie(5)
        db.get_movie_by_category("Action")
        print(f"Le nombre total de tickets vendus est de \033[92m{db.get_total_tickets_sold()}\033[0m")
        db.get_movie_by_director("Steven Spielberg")
        db.get_top_movies_by_tickets_sold(5)
        db.get_top_cinema_by_tickets_sold(5)
        db.get_movie_name_under_price(15, 10)
        db.delete_films_with_director("Steven Spielberg")
    except Exception as e:
        print("\033[91mServeur non disponible\033[97m ->", e)
        exit(1)
