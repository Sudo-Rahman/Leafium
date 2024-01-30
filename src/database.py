import math
import random

import pymongo

from src.data import *


class Database:
    def __init__(self, host: str, port: int, database: str, user: str = None, password: str = None):
        self.db = pymongo.MongoClient(host, port)[database]
        if user and password:
            self.db.authenticate(user, password)

    def populate(self, film: int):

        for i in range(film):
            self.insert_film({
                "release_date": f"20{math.floor(random.random() * 24)}-01-01",
                "title": titres_de_films[math.floor(random.random() * len(titres_de_films))],
                "duration": math.floor(random.random() * 100) + 60,
                "description": ''.join(random.choice('abcdefghijklmnopqrstuvyxyz') for _ in range(100)),
                "directors": [realisateurs_de_films[math.floor(random.random() * len(realisateurs_de_films))] for _ in
                              range(math.floor(random.random() * 3))],
                "categories": [genres_de_films[math.floor(random.random() * len(genres_de_films))] for _ in
                               range(math.floor(random.random() * 10))],
                "comments": [
                    {
                        "author": users[math.floor(random.random() * len(users))],
                        **commentaires_et_notes_de_films[math.floor(random.random() * len(commentaires_et_notes_de_films))]
                    } for _ in range(math.floor(random.random() * 100))
                ]
            })

        films_id_list = [film["_id"] for film in self.get_films({}, {"_id": 1})]

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
                                "_id_film": films_id_list[math.floor(random.random() * len(films_id_list))],
                                "date_broadcast": f"{math.floor(random.random() * 30)}/{math.floor(random.random() * 12)}/20{math.floor(random.random() * 24)} {math.floor(random.random() * 14 + 10)}:00:00",
                                "price": math.floor(random.random() * 10) + 5,
                                "ticket_sold": math.floor(random.random() * capacity)
                            } for _ in range(math.floor(random.random() * 100))
                        ]
                    } for i in range(math.floor(random.random() * 10))
                ]
            })

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
