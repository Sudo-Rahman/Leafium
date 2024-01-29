import pymongo


class Database:
    def __init__(self, host: str, port: int, database: str):
        self.db = pymongo.MongoClient(host, port)[database]

    def populate(self, n: int):
        for i in range(n):
            pass

    def get_all(self):
        return self.db.film.find()

    def get_by_title(self, title: str):
        return self.db.film.find_one({"title": title})

    def get_by_year(self, year: int):
        return self.db.film.find_one({"year": year})

    def get_by_genre(self, genre: str):
        return self.db.film.find_one({"genre": genre})

    def get_by_director(self, director: str):
        return self.db.film.find_one({"director": director})

    def get_by_country(self, country: str):
        return self.db.film.find_one({"country": country})

    def get_by_duration(self, duration: int):
        return self.db.film.find_one({"duration": duration})

    def get_by_id(self, id: str):
        return self.db.film.find_one({"_id": id})

    def insert(self, film: dict):
        self.db.film.insert_one(film)

    def update(self, id: str, film: dict):
        self.db.film.update_one({"_id": id}, {"$set": film})
