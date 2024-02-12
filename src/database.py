import math
import random
from time import sleep

import matplotlib.pyplot as plt
import pymongo

from data import *


class Database:

    def __init__(self, host: str, port: int, database: str, user: str = None, password: str = None):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.db = None

        if host == "mongo2.iem":
            self.db = pymongo.MongoClient(host, port, username="mc150904", password="mc150904", authSource="mc150904",
                                          authMechanism="SCRAM-SHA-1")[database]
        else:
            self.db = pymongo.MongoClient(host, port)[database]
            if user and password:
                self.db.authenticate(user, password)

    def create_collection_cinemas(self):
        """
        Crée la collection cinemas.
        :param self:
        :return: None
        """
        self.db.create_collection("cinemas", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "address", "rooms"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "Nom du cinéma"
                    },
                    "address": {
                        "bsonType": "object",
                        "required": ["city", "number", "street", "zip"],
                        "properties": {
                            "city": {
                                "bsonType": "string",
                                "description": "Ville"
                            },
                            "number": {
                                "bsonType": "int",
                                "description": "Numéro"
                            },
                            "street": {
                                "bsonType": "string",
                                "description": "Rue"
                            },
                            "zip": {
                                "bsonType": "int",
                                "description": "Code postal"
                            }
                        }
                    },
                    "rooms": {
                        "bsonType": "array",
                        "description": "Salles",
                        "items": {
                            "bsonType": "object",
                            "required": ["name", "capacity", "broadcasts"],
                            "properties": {
                                "name": {
                                    "bsonType": "string",
                                    "description": "Nom de la salle"
                                },
                                "capacity": {
                                    "bsonType": "int",
                                    "description": "Capacité de la salle"
                                },
                                "broadcasts": {
                                    "bsonType": "array",
                                    "description": "Diffusions",
                                    "items": {
                                        "bsonType": "object",
                                        "required": ["film", "date_broadcast", "price", "ticket_sold"],
                                        "properties": {
                                            "film": {
                                                "bsonType": "object",
                                                "required": ["name", "_id"],
                                                "properties": {
                                                    "_id": {
                                                        "bsonType": "objectId",
                                                        "description": "l'id du film"
                                                    },
                                                    "name": {
                                                        "bsonType": "string",
                                                        "description": "nom du film"
                                                    },
                                                }
                                            },
                                            "date_broadcast": {
                                                "bsonType": "string",
                                                "description": "Date de diffusion"
                                            },
                                            "price": {
                                                "bsonType": "int",
                                                "description": "Prix de la place"
                                            },
                                            "ticket_sold": {
                                                "bsonType": "int",
                                                "description": "Nombre de tickets vendus"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        })

    def create_collection_films(self):
        """
        Crée la collection films.
        :param self:
        :return: None
        """
        self.db.create_collection("films", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["release_date", "title", "duration", "description", "directors", "categories", "comments"],
                "properties": {
                    "release_date": {
                        "bsonType": "string",
                        "description": "Date de sortie"
                    },
                    "title": {
                        "bsonType": "string",
                        "description": "Titre du film"
                    },
                    "duration": {
                        "bsonType": "int",
                        "description": "Durée du film"
                    },
                    "description": {
                        "bsonType": "string",
                        "description": "Description du film"
                    },
                    "directors": {
                        "bsonType": "array",
                        "description": "Réalisateurs",
                        "items": {
                            "bsonType": "string",
                            "description": "Nom du réalisateur"
                        }
                    },
                    "categories": {
                        "bsonType": "array",
                        "description": "Catégories",
                        "items": {
                            "bsonType": "string",
                            "description": "Nom de la catégorie"
                        }
                    },
                    "comments": {
                        "bsonType": "array",
                        "description": "Commentaires",
                        "items": {
                            "bsonType": "object",
                            "required": ["author", "content", "rating"],
                            "properties": {
                                "author": {
                                    "bsonType": "string",
                                    "description": "Auteur du commentaire"
                                },
                                "content": {
                                    "bsonType": "string",
                                    "description": "Commentaire"
                                },
                                "rating": {
                                    "bsonType": "int",
                                    "description": "Note du film"
                                }
                            }
                        }
                    }
                }
            }
        })

    def drop_collection(self):
        """
        Permet de supprimer les collections films et cinemas.
        :param self:
        :return: None
        """
        self.db["films"].drop()
        self.db["cinemas"].drop()
        print("Collections films et cinemas supprimées")

    def populate(self, film: int):
        """
        Permet de peupler la base de données avec des films et des cinémas.
        :param film: Nombre de films à insérer
        :return: None
        """
        # Création des collections films et cinemas
        list_collection_names = self.db.list_collection_names()
        if not ("films" in list_collection_names and "cinemas" in list_collection_names):
            self.create_collection_cinemas()
            self.create_collection_films()
            sleep(1)

        for i in range(film):
            self.insert_film({
                "release_date": f"20{math.floor(random.random() * 24)}-01-01",
                "title": titres_de_films[math.floor(random.random() * len(titres_de_films))],
                "duration": math.floor(random.random() * 100) + 60,
                "description": ''.join(random.choice('abcdefghijklmnopqrstuvyxyz') for _ in range(100)),
                "directors": [realisateurs_de_films[math.floor(random.random() * len(realisateurs_de_films))] for _
                              in
                              range(math.floor(random.random() * 3))],
                "categories": [genres_de_films[math.floor(random.random() * len(genres_de_films))] for _ in
                               range(math.floor(random.random() * 10))],
                "comments": [
                    {
                        "author": users[math.floor(random.random() * len(users))],
                        **commentaires_et_notes_de_films[
                            math.floor(random.random() * len(commentaires_et_notes_de_films))]
                    } for _ in range(math.floor(random.random() * film))
                ]
            })

        films_id_list = [{"_id": film["_id"], "name": film["title"]} for film in
                         self.get_films({}, {"_id": 1, "title": 1})]

        for cinama in cinemas:
            capacity = math.floor(random.random() * 500)
            self.insert_cinema({
                **cinama,
                "rooms": [
                    {
                        "name": f"room{i}",
                        "capacity": capacity,
                        "broadcasts": [
                            {
                                "film": films_id_list[math.floor(random.random() * len(films_id_list))],
                                "date_broadcast": f"{math.floor(random.random() * 30)}/{math.floor(random.random() * 12)}/20{math.floor(random.random() * 24)} {math.floor(random.random() * 14 + 10)}:00:00",
                                "price": math.floor(random.random() * 10) + 5,
                                "ticket_sold": math.floor(random.random() * capacity)
                            } for _ in range(math.floor(random.random() * 100))
                        ]
                    } for i in range(math.floor(random.random() * 10))
                ]
            })

    def clear(self):
        """
        Permet de vider la base de données.
        :param self:
        :return: None
        """
        self.db["films"].delete_many({})
        self.db["cinemas"].delete_many({})
        print("Base de données vidée")

    ##########################
    #    FONCTIONS DE BASE   #
    ##########################

    def get(self, collection: str, query: dict = None, projection: dict = None):
        if query is None:
            query = {}
        if projection is None:
            projection = {}
        return self.db[collection].find(query, projection)

    def get_one(self, collection: str, query: dict = None, projection: dict = None):
        if query is None:
            query = {}
        if projection is None:
            projection = {}
        return self.db[collection].find_one(query, projection)

    def get_films(self, query: dict = None, projection: dict = None):
        return self.get("films", query, projection)

    def get_cinemas(self, query: dict = None, projection: dict = None):
        return self.get("cinemas", query, projection)

    def get_film(self, query: dict = None, projection: dict = None):
        return self.get_one("films", query, projection)

    def get_cinema(self, query: dict = None, projection: dict = None):
        return self.get_one("cinemas", query, projection)

    def insert(self, collection: str, document: dict):
        return self.db[collection].insert_one(document)

    def insert_many(self, collection: str, documents: list):
        return self.db[collection].insert_many(documents)

    def update(self, collection: str, query: dict, update: dict):
        return self.db[collection].update_one(query, update)

    def insert_film(self, film: dict):
        return self.insert("films", film)

    def insert_films(self, films: list):
        return self.insert_many("films", films)

    def insert_cinema(self, cinema: dict):
        return self.insert("cinemas", cinema)

    def insert_cinemas(self, cinemas: list):
        return self.insert_many("cinemas", cinemas)

    ##########################
    # FONCTIONS DE REQUÊTES  #
    ##########################

    def get_average_rating_by_movie(self, limit: int):
        """
        Récupère la moyenne des notes des films.
        :param self:
        :param limit: Le nombre de films à afficher.
        :return: La moyenne des notes des films.
        """
        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$unwind": "$comments"},
                {"$group": {"_id": "$_id", "title": {"$first": "$title"},
                            "average_rating": {"$avg": "$comments.rating"}}},
                {"$sort": {"average_rating": -1}},
                {"$limit": limit + 1}
            ]

            data = list(self.db["films"].aggregate(pipeline))
            titles = [movie['title'] for movie in data]
            ratings = [movie['average_rating'] for movie in data]

            plt.figure(figsize=(12, 8))
            plt.bar(titles, ratings, color='skyblue', edgecolor='black', linewidth=1.2)
            plt.xlabel('Nom des films', fontsize=14)
            plt.ylabel('Moyenne des notes', fontsize=14)
            plt.title(f'Top des {limit} films', fontsize=16)
            plt.xticks(rotation=45, ha='right', fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_movie_by_category(self, category: str):
        """
        Récupère les films de la catégorie donnée.
        :param self:
        :param category: Le nom de la catégorie.
        :return: Les films de la catégorie donnée.
        """
        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$match": {"categories": category}},
                {"$project": {"title": 1, "categories": 1}},
                {"$sort": {"title": 1}},
                {"$limit": 10}
            ]

            data = list(self.db["films"].aggregate(pipeline))
            titles = [movie['title'] for movie in data]
            categories = [movie['categories'] for movie in data]
            print("Les films de la catégorie", category, "sont:")
            for i in range(len(titles)):
                title = f"\033[92m{titles[i]}\033[0m"
                category_text = f"{'catégories' if len(categories[i]) > 1 else 'catégorie'}"
                category = f"\033[94m{', '.join(categories[i])}\033[0m"
                print(f"{title} avec comme {category_text} {category}")

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_movie_by_director(self, director: str):
        """
        Récupère les films réalisés par un réalisateur donné.
        :param self:
        :param director: Le nom du réalisateur.
        :return: Les films réalisés par le réalisateur donné.
        """

        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$match": {"directors": director}},
                {"$project": {"title": 1, "directors": 1}},
                {"$sort": {"title": 1}}
            ]

            data = list(self.db["films"].aggregate(pipeline))
            titles = [movie['title'] for movie in data]
            directors = [movie['directors'] for movie in data]
            print("Les films du réalisateur", director, "sont:")
            for i in range(len(titles)):
                title = f"\033[92m{titles[i]}\033[0m"
                director_text = f"{'réalisateurs' if len(directors[i]) > 1 else 'réalisateur'}"
                director = f"\033[94m{', '.join(directors[i])}\033[0m"
                print(f"{title} avec comme {director_text} {director}")

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_total_tickets_sold(self):
        """
        Récupère le nombre total de tickets vendus.
        :param self:
        :return: Le nombre total de tickets vendus.
        """

        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")
            pipeline = [
                {"$unwind": "$rooms"},
                {"$unwind": "$rooms.broadcasts"},
                {"$group": {"_id": 'Max', "total_tickets_sold": {"$sum": "$rooms.broadcasts.ticket_sold"}}}
            ]
            data = list(self.db["cinemas"].aggregate(pipeline))
            total_tickets_sold = data[0]['total_tickets_sold']
            # print(f"Le nombre total de tickets vendus est de \033[92m{total_tickets_sold}\033[0m")
            return total_tickets_sold

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_top_movies_by_tickets_sold(self, limit: int):
        """
        Récupère les films ayant vendu le plus de tickets.
        :param self:
        :param limit:
        :return:
        """
        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$unwind": "$rooms"},
                {"$unwind": "$rooms.broadcasts"},
                {"$group": {"_id": "$rooms.broadcasts.film._id",
                            "name": {"$first": "$rooms.broadcasts.film.name"},
                            "total_tickets_sold": {"$sum": "$rooms.broadcasts.ticket_sold"}}},
                {"$sort": {"total_tickets_sold": -1}},
                {"$limit": limit}
            ]

            data = list(self.db["cinemas"].aggregate(pipeline))
            titles = [movie['name'] for movie in data]
            tickets_sold = [movie['total_tickets_sold'] for movie in data]
            print(f"Les {limit} films ayant vendu le plus de tickets sont:")
            for i in range(len(titles)):
                title = f"\033[92m{titles[i]}\033[0m"
                tickets_sold_text = f"{'tickets vendus' if tickets_sold[i] > 1 else 'ticket vendu'}"
                tickets_sold_number = f"\033[94m{tickets_sold[i]}\033[0m"
                print(f"{title} avec \033[94m{tickets_sold[i]}\033[0m {tickets_sold_text}")
            sum_tickets_sold = sum(tickets_sold)
            total_tickets_sold = self.get_total_tickets_sold()
            title_string = "Diagramme des parts de marché des " + str(total_tickets_sold) + " tickets vendus par film"
            valeurs = tickets_sold + [self.get_total_tickets_sold() - sum_tickets_sold]
            etiquettes = titles + ['Autres']
            plt.pie(valeurs, labels=etiquettes, autopct='%1.1f%%', startangle=90)
            plt.title(title_string)
            plt.show()

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_top_cinema_by_tickets_sold(self, limit: int):
        """
        Récupère les cinémas ayant vendu le plus de tickets.
        :param self:
        :param limit: Le nombre de cinémas à afficher.
        :return: Les cinémas ayant vendu le plus de tickets.
        """
        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$unwind": "$rooms"},
                {"$unwind": "$rooms.broadcasts"},
                {"$group": {"_id": "$_id",
                            "name": {"$first": "$name"},
                            "total_tickets_sold": {"$sum": "$rooms.broadcasts.ticket_sold"}}},
                {"$sort": {"total_tickets_sold": -1}},
                {"$limit": limit}
            ]

            data = list(self.db["cinemas"].aggregate(pipeline))
            names = [cinema['name'] for cinema in data]
            tickets_sold = [cinema['total_tickets_sold'] for cinema in data]
            print(f"Les {limit} cinémas ayant vendu le plus de tickets sont:")
            for i in range(len(names)):
                name = f"\033[92m{names[i]}\033[0m"
                tickets_sold_text = f"{'tickets vendus' if tickets_sold[i] > 1 else 'ticket vendu'}"
                print(f"{name} avec \033[94m{tickets_sold[i]}\033[0m {tickets_sold_text}")

            sum_tickets_sold = sum(tickets_sold)
            total_tickets_sold = self.get_total_tickets_sold()
            title_string = "Diagramme des parts de marché des " + str(total_tickets_sold) + " tickets vendus"
            valeurs = tickets_sold + [self.get_total_tickets_sold() - sum_tickets_sold]
            etiquettes = names + ['Autres']
            plt.pie(valeurs, labels=etiquettes, autopct='%1.1f%%', startangle=90)
            plt.title(title_string)
            plt.show()

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

    def get_movie_name_under_price(self, price: int, limit: int):
        """
        Récupère les films dont le prix est inférieur à celui donné.
        :param self:
        :param limit: Le nombre de films à afficher.
        :param price: Le prix maximum.
        :return: Les films dont le prix est inférieur à celui donné.
        """
        try:
            if self.db is None:
                raise ValueError("Erreur de connexion à la base de données")

            pipeline = [
                {"$unwind": "$rooms"},
                {"$unwind": "$rooms.broadcasts"},
                {"$match": {"rooms.broadcasts.price": {"$lt": price}}},
                {"$group": {"_id": "$rooms.broadcasts.film._id", "name": {"$first": "$rooms.broadcasts.film.name"},
                            "prix": {"$first": "$rooms.broadcasts.price"}}},
                {"$sort": {"prix": -1}},
                {"$limit": limit}
            ]

            data = list(self.db["cinemas"].aggregate(pipeline))
            titles = [movie['name'] for movie in data]
            prices = [movie['prix'] for movie in data]
            print(f"Les {limit} films dont le prix est inférieur à \033[92m{price}$\033[0m sont:\033[0m")
            for i in range(len(titles)):
                title = f"\033[92m{titles[i]}\033[0m"
                price_text = f"{'prix' if prices[i] > 1 else 'prix'}"
                print(f"{title} avec un \033[94m{prices[i]}$\033[0m {price_text}")

            plt.figure(figsize=(12, 8))
            plt.bar(titles, prices, color='skyblue', edgecolor='black', linewidth=1.2)
            plt.xlabel('Nom des films', fontsize=14)
            plt.ylabel('Prix', fontsize=14)
            plt.title(f'Top des {limit} films dont le prix est inférieur à {price}$', fontsize=16)
            plt.xticks(rotation=45, ha='right', fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None

