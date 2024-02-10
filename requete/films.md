<h1 align="center">Films</h1>

Structure de validation de la collection films.

```python
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
```