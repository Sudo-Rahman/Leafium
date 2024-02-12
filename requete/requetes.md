### Requête 1 : afficher le cinema UGC Ciné Cité Les Halles :

```js
db.cinemas.find({
    "name": "UGC Ciné Cité Les Halles"
}).pretty()
```

### Requête 2 : afficher le nombre de salle de chaque cinema

```js
db.cinemas.aggregate([{
    $project: {
        _id: 0,
        name: 1,
        nb_salle: {
            $size: "$rooms"
        }
    }
}])
```

### Requête 3 : afficher le nombre de siege de chaque cinena

```js
db.cinemas.aggregate([{
    $project: {
        _id: 0,
        name: 1,
        nb_siege: {
            $sum: "$rooms.capacity"
        }
    }
}])
```

### Requête 4 :  afficher le nombre de diffusion de chaque cinema

```js
db.cinemas.aggregate([{
    $project: {
        _id: 0,
        name: 1,
        nb_diffusion: {
            $sum: {
                $map: {
                    input: "$rooms",
                    as: "room",
                    in: {
                        $size: "$$room.broadcasts"
                    }
                }
            }
        }
    }
}])
```

### Requête 5 : afficher le nombre de ticket vendu par cinema

```js
db.cinemas.aggregate([{
    $project: {
        _id: 0,
        name: 1,
        nb_ticket: {
            $sum: {
                $map: {
                    input: "$rooms",
                    as: "room",
                    in: {
                        $sum: "$$room.broadcasts.ticket_sold"
                    }
                }
            }
        }
    }
}])
```

### Requête 6 : afficher le chiffre d'affaire de chaque cinema

```js
db.cinemas.aggregate([{
    $project: {
        _id: 0,
        name: 1,
        chiffre_affaire: {
            $sum: {
                $map: {
                    input: "$rooms",
                    as: "room",
                    in: {
                        $sum: {
                            $map: {
                                input: "$$room.broadcasts",
                                as: "broadcast",
                                in: {
                                    $multiply: ["$$broadcast.ticket_sold", "$$broadcast.price"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}])
```

### Requête 7 : afficher l'id du film ainsi que sa recette pour le film qui a fait le plus de recette

```js
db.cinemas.aggregate([
    {
        $project: {
            _id: 0,
            name: 1,
            chiffre_affaire: {
                salle: {
                    $map: {
                        input: "$rooms",
                        as: "room",
                        in: {
                            film: {
                                $map: {
                                    input: "$$room.broadcasts",
                                    as: "broadcast",
                                    in: {
                                        _id_film: "$$broadcast.film._id",
                                        recette: {
                                            $multiply: ["$$broadcast.ticket_sold", "$$broadcast.price"]
                                        },
                                        name: "$$broadcast.film.name",
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    {
        $unwind: "$chiffre_affaire.salle"
    },
    {
        $unwind: "$chiffre_affaire.salle.film"
    },
    {
        $group: {
            _id: "$chiffre_affaire.salle.film._id_film",
            recette: {
                $sum: "$chiffre_affaire.salle.film.recette",
            },
            name: {
                $first: "$chiffre_affaire.salle.film.name"
            }
        }
    },
    {
        $sort: {
            recette: -1
        }
    },
    {
        $limit: 1
    }
])
```

### Requête 8 : afficher les films qui ont une durée supérieur à 2h et qui sont dans les catégories "Fantasy" ou "Comédie"

```js
db.films.find({
    duration: {$gt: 120}, categories: {$in: ["Fantasy", "Comédie"]}
}, {
    title: 1, duration: 1, categories: 1, "comments.rating": 1
},).sort({duration: -1}).pretty()
```

### Requête 9 : mettre à jour le film "Gangs of New York" en ajoutant les catégories "Crime" et "Drama" et en modifiant

sa description

```js
db.films.updateOne({title: "Gangs of New York"}, {
    $set: {
        categories: ["Crime", "Drama"],
        description: "L'historie de la vie de Bill le Boucher, un chef de gang irlandais à New York dans les années 1860.",
    },
});
```

### Requête 10 : tous les films avec le réalisateur "George Lucas"

```js
db.films.find({directors: "George Lucas"}, {title: 1, _id: 0})
```

### Requête 11 : insérer un nouveau cinema à Beaune avec une salle de 200 places

```js
db.cinemas.insertOne({
    name: "Cinema Beaune",
    address: {
        street: "Rue de la République",
        city: "Beaune",
        zip: 21200,
        number: 1
    },
    rooms: [
        {
            name: "Salle 1",
            capacity: 200,
            broadcasts: []
        }
    ]
})
```

### Requête 12 : supprimer tous les cinemas de Paris

```js
db.cinemas.deleteMany({"address.city": "Paris"})
```

### Requête 13 : afficher le top 10 des films qui ont fait le plus d'entrée

```js
db.cinemas.aggregate([
    {
        $project: {
            _id: 0,
            name: 1,
            _: {
                $map: {
                    input: "$rooms",
                    as: "room",
                    in: {
                        film: {
                            $map: {
                                input: "$$room.broadcasts",
                                as: "broadcast",
                                in: {
                                    _id_film: "$$broadcast.film._id",
                                    entree: "$$broadcast.ticket_sold",
                                    name: "$$broadcast.film.name",
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    {
        $unwind: "$_"
    },
    {
        $unwind: "$_.film"
    },
    {
        $group: {
            _id: "$_.film._id_film",
            entree: {
                $sum: "$_.film.entree"
            },
            name: {
                $first: "$_.film.name"
            }
        }
    },
    {
        $sort: {
            entree: -1
        }
    },
    {
        $limit: 10
    }
])
```

### Requête 14 : afficher les films avec leur nombre de commentair trier par ordre decroissant

```js
db.films.aggregate([{
    $project: {
        _id: 0,
        title: 1,
        nb_commentaire: {
            $size: "$comments"
        }
    }
},
    {
        $sort: {
            nb_commentaire: -1
        }
    }
])
```

### Requête 15 : afficher le top 10 des films avec la meilleur moyenne de note

```js
db.films.aggregate([
    {
        $project: {
            _id: 0,
            moyenne_note: {
                $avg: "$comments.rating"
            },
            document: "$$ROOT",
        }
    },
    {
        $sort: {
            moyenne_note: -1
        }
    },
    {
        $limit: 10
    },
])
```

### Requête 16 : Map Reduce pour afficher le nombre de ticket vendu par cinema

```js
db.cinemas.mapReduce(
    function () {
        this.rooms.forEach(function (room) {
            var nb_ticket = 0;
            room.broadcasts.forEach(function (broadcast) {
                nb_ticket += broadcast.ticket_sold;
            });
            emit(this.name, nb_ticket);
        });
    },
    function (key, values) {
        return Array.sum(values);
    },
    {
        out: "nb_ticket"
    }
)
```

### Requête 17 : Mise à jour de la collection cinema pour ajouter un champ "nb_ticket" qui contient le nombre de ticket vendu par cinema

```js
db.cinemas.aggregate([
    {
        $project: {
            _id: 0,
            name: 1,
            nb_ticket: {
                $sum: {
                    $map: {
                        input: "$rooms",
                        as: "room",
                        in: {
                            $sum: "$$room.broadcasts.ticket_sold"
                        }
                    }
                }
            }
        }
    }
]).forEach(function (cinema) {
    db.cinemas.updateOne({name: cinema.name}, {
        $set: {
            nb_ticket: cinema.nb_ticket
        }
    });
});
```

### Requête 18 : Passer les notes des commentaires entre 0 et 5 à entre 0 et 20

```js
db.films.find({}).forEach(function (film) {
    film.comments.forEach(function (comment) {
        comment.rating *= 4
        db.films.updateOne({_id: film._id}, {$set: {comments: film.comments}})
    })
})
```