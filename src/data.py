genres_de_films = ["Action", "Comédie", "Drame", "Science-fiction", "Horreur", "Documentaire", "Animation",
                   "Romance", "Thriller", "Fantasy", "Aventure", "Mystère", "Crime", "Familial", "Guerre", "Histoire"]

realisateurs_de_films = ["Christopher Nolan", "Quentin Tarantino", "Steven Spielberg", "Martin Scorsese",
                         "Alfred Hitchcock", "Francis Ford Coppola", "Stanley Kubrick", "David Fincher",
                         "Sofia Coppola", "Greta Gerwig", "James Cameron", "George Lucas", "Peter Jackson",
                         "Tim Burton"]

users = [
    "Jean", "Pierre", "Paul", "Jacques", "Marie", "Julie", "Sophie", "Alice", "Lucie", "Emma", "Louise", "Léa", "Chloé"]

titres_de_films = [
    "Inception",
    "Pulp Fiction",
    "Jurassic Park",
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Titanic",
    "Forrest Gump",
    "The Matrix",
    "La La Land",
    "Avatar",
    "Star Wars: Episode IV - A New Hope",
    "Casablanca",
    "Gone with the Wind",
    "The Silence of the Lambs",
    "The Lord of the Rings: The Return of the King",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers",
    "The Lion King",
    "The Avengers",
    "The Sixth Sense",
    "The Social Network",
    "The Departed",
    "The Prestige",
    "The Green Mile",
    "The Shining",
    "The Great Gatsby",
    "La boite noire",
    "Le voyage de Chihiro",
    "Le loup de Wall Street",
]

commentaires_et_notes_de_films = [
    {"content": "Captivant du début à la fin, un incontournable !", "rating": 5},
    {"content": "Une histoire émotionnelle qui vous fait réfléchir.", "rating": 4},
    {"content": "Les performances des acteurs sont exceptionnelles.", "rating": 5},
    {"content": "L'intrigue est bien construite, avec des rebondissements inattendus.", "rating": 4},
    {"content": "La réalisation est visuellement époustouflante.", "rating": 5},
    {"content": "Une bande sonore qui ajoute beaucoup à l'expérience cinématographique.", "rating": 4},
    {"content": "Des effets spéciaux incroyables qui immergent le spectateur dans un autre monde.", "rating": 5},
    {"content": "Un mélange parfait d'action, de suspense et d'émotion.", "rating": 4},
    {"content": "Le scénario est original et bien écrit.", "rating": 5},
    {"content": "Un casting fantastique qui donne vie aux personnages.", "rating": 4},
    {"content": "La direction artistique et les décors sont remarquables.", "rating": 5},
    {"content": "Un film qui laisse une impression durable après sa visualisation.", "rating": 4},
    {"content": "Une exploration intelligente de thèmes profonds et pertinents.", "rating": 5},
    {"content": "Une comédie hilarante qui vous fait rire du début à la fin.", "rating": 4},
    {"content": "Les dialogues sont percutants et mémorables.", "rating": 5},
    {"content": "Un film qui offre une perspective unique sur un sujet particulier.", "rating": 4},
    {"content": "La cinématographie est superbe, chaque plan est soigneusement composé.", "rating": 5},
    {"content": "Une expérience cinématographique qui mérite d'être partagée avec d'autres.", "rating": 4},
    {"content": "Un chef-d'œuvre du genre [ajouter le genre du film].", "rating": 5},

    {"content": "Ennuyeux du début à la fin, évitez-le !", "rating": 0},
    {"content": "Une histoire sans intérêt qui ne provoque aucune émotion.", "rating": 1},
    {"content": "Les performances des acteurs sont médiocres.", "rating": 2},
    {"content": "L'intrigue est prévisible et décevante.", "rating": 1},
    {"content": "La réalisation est terne et sans inspiration.", "rating": 0},
    {"content": "Une bande sonore qui ne parvient pas à sauver le film.", "rating": 1},
    {"content": "Effets spéciaux décevants, loin d'immerger le spectateur.", "rating": 0},
    {"content": "Un mélange raté d'action, de suspense et d'émotion.", "rating": 1},
    {"content": "Le scénario est cliché et mal exécuté.", "rating": 0},
    {"content": "Un casting qui ne parvient pas à sauver le naufrage.", "rating": 1},
    {"content": "La direction artistique et les décors sont médiocres.", "rating": 0},
    {"content": "Un film que vous oublierez dès la fin.", "rating": 1},
    {"content": "Une exploration superficielle de thèmes sans intérêt.", "rating": 0},
    {"content": "Une comédie qui ne fait rire personne.", "rating": 1},
    {"content": "Les dialogues sont plats et sans intérêt.", "rating": 0},
    {"content": "Un film dépourvu de toute perspective unique.", "rating": 1},
    {"content": "La cinématographie est médiocre, chaque plan est banal.", "rating": 0},
    {"content": "Une expérience cinématographique à éviter à tout prix.", "rating": 1},
    {"content": "Un désastre du genre [ajouter le genre du film].", "rating": 0}
]

cinemas = [
    {
        "name": "UGC Ciné Cité Les Halles",
        "address": {
            "street": "Place de la Rotonde",
            "number": 7,
            "city": "Paris",
            "zip": 75001
        }
    },
    {
        "name": "Gaumont Opéra Capucines",
        "address": {
            "street": "Boulevard Montmartre",
            "number": 2,
            "city": "Paris",
            "zip": 75009
        }
    },
    {
        "name": "Pathé Wepler",
        "address": {
            "street": "Boulevard de Clichy",
            "number": 140,
            "city": "Paris",
            "zip": 75018
        }
    },
    {
        "name": "MK2 Bibliothèque",
        "address": {
            "street": "Avenue de France",
            "number": 128,
            "city": "Paris",
            "zip": 75013
        }
    },
    {
        "name": "Le Grand Rex",
        "address": {
            "street": "Boulevard Poissonnière",
            "number": 1,
            "city": "Paris",
            "zip": 75002
        }
    },
    {
        "name": "UGC Ciné Cité Bercy",
        "address": {
            "street": "Cour Saint-Émilion",
            "number": 2,
            "city": "Paris",
            "zip": 75012
        }
    },
    {
        "name": "Pathé La Villette",
        "address": {
            "street": "Avenue Corentin Cariou",
            "number": 30,
            "city": "Paris",
            "zip": 75019
        }
    },
    {
        "name": "Le Louxor - Palais du Cinéma",
        "address": {
            "street": "Boulevard de Magenta",
            "number": 170,
            "city": "Paris",
            "zip": 75010
        }
    },
    {
        "name": "MK2 Quai de Seine",
        "address": {
            "street": "Quai de la Seine",
            "number": 14,
            "city": "Paris",
            "zip": 75019
        }
    },
    {
        "name": "Cinéma des Cinéastes",
        "address": {
            "street": "Avenue de Clichy",
            "number": 7,
            "city": "Paris",
            "zip": 75017
        }
    }
]
