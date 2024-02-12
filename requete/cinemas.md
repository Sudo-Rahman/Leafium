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
```

### Exemple de document

```json
{
  "name": "Cinéma Le Rex",
  "address": {
    "city": "Paris",
    "number": 1,
    "street": "Boulevard",
    "zip": 75000
  },
  "rooms": [
    {
      "name": "Salle 1",
      "capacity": 100,
      "broadcasts": [
        {
          "film": {
            "_id": ObjectId("5f5f3e3e3e3e3e3e3e3e3e3e"),
            "name": "avanger"
          },
          "date_broadcast": "2020-01-01",
          "price": 10,
          "ticket_sold": 100
        }
      ]
    }
  ]
}
```