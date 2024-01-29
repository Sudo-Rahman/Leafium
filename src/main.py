import pymongo
from database import Database


if __name__ == '__main__':
    db = Database("localhost", 27017, "leafium")
    db.populate(10)