<h1 align="center">Cinemas</h1>

Structure de validation de la collection cinemas

```python
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
                                "required": ["_id_film", "date_broadcast", "price", "ticket_sold"],
                                "properties": {
                                    "_id_film": {
                                        "bsonType": "objectId",
                                        "description": "ID du film"
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
```