genres_de_films = ["Action", "Comédie", "Drame", "Science-fiction", "Horreur", "Documentaire", "Animation",
                   "Romance", "Thriller", "Fantasy", "Aventure", "Mystère", "Crime", "Familial", "Guerre", "Histoire"]

realisateurs_de_films = ["Christopher Nolan", "Quentin Tarantino", "Steven Spielberg", "Martin Scorsese",
                         "Alfred Hitchcock", "Francis Ford Coppola", "Stanley Kubrick", "David Fincher",
                         "Sofia Coppola", "Greta Gerwig", "James Cameron", "George Lucas", "Peter Jackson",
                         "Tim Burton", "Ridley Scott", "Clint Eastwood", "Woody Allen", "Wes Anderson", "Spike Lee",
                         "Sergio Leone",
                         "Hayao Miyazaki", "Jean-Luc Godard", "Akira Kurosawa", "David Lynch", "Ingmar Bergman",
                         "Federico Fellini",
                         "Charlie Chaplin", "Roman Polanski", "Quentin Tarantino", "Stanley Kubrick",
                         "Alfred Hitchcock",
                         "Martin Scorsese", "Steven Spielberg", "Christopher Nolan", "David Fincher",
                         "Francis Ford Coppola",
                         "Peter Jackson", "Woody Allen", "Tim Burton", "Clint Eastwood", "James Cameron",
                         "Coen Brothers"
                         ]

users = [
    "Jean", "Pierre", "Paul", "Jacques", "Marie", "Julie", "Sophie", "Alice", "Lucie", "Emma", "Louise", "Léa", "Chloé",
    "Léo", "Louis", "Hugo", "Arthur", "Raphaël", "Ethan", "Maël", "Gabriel", "Jules", "Adam", "Lucas", "Noah", "Liam",
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Emily",
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher",
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy",
    "Mohamed", "Adam", "Liam", "Noah", "Ethan", "Lucas", "Mason", "Logan", "Oliver", "James", "Alexander", "Elijah",
    "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Abigail", "Emily", "Harper", "Amelia", "Evelyn", "Elizabeth",
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hector", "Isabel", "Jack", "Katherine", "Liam", "Mia",
    "Nathan", "Olivia", "Pablo", "Quinn", "Rachel", "Samuel", "Taylor", "Ulysses", "Victoria", "William", "Xavier",
    "Yvonne", "Zachary"
]

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
    {"content": "Un film qui vous fera réfléchir longtemps après sa visualisation.", "rating": 4},
    {"content": "Une histoire émouvante qui vous fera verser des larmes.", "rating": 5},
    {"content": "Les performances des acteurs sont exceptionnelles.", "rating": 4},
    {"content": "L'intrigue est bien construite, avec des rebondissements inattendus.", "rating": 5},
    {"content": "La réalisation est visuellement époustouflante.", "rating": 4},
    {"content": "Une bande sonore qui ajoute beaucoup à l'expérience cinématographique.", "rating": 5},
    {"content": "Des effets spéciaux incroyables qui immergent le spectateur dans un autre monde.", "rating": 4},
    {"content": "La fin est trop longue mais le film est bien", "rating": 3},
    {"content": "Un mélange parfait d'action, de suspense et d'émotion.", "rating": 5},
    {"content": "Le scénario est original et bien écrit.", "rating": 4},
    {"content": "Un casting fantastique qui donne vie aux personnages.", "rating": 5},
    {"content": "La fin est inattendue, ce qui rend le film passionnant.", "rating": 4},
    {"content": "Une performance exceptionnelle des acteurs principaux.", "rating": 5},
    {"content": "Le rythme du film est un peu lent, mais l'histoire est captivante.", "rating": 3},
    {"content": "Effets spéciaux époustouflants, surtout dans les scènes d'action.", "rating": 4},
    {"content": "Dialogues intelligents et bien écrits.", "rating": 4},
    {"content": "Les décors sont magnifiques, ajoutant une dimension visuelle unique.", "rating": 5},
    {"content": "Le film a un message puissant et poignant.", "rating": 5},
    {"content": "Bande sonore exceptionnelle qui accompagne parfaitement l'histoire.", "rating": 5},
    {"content": "Certaines scènes manquent de crédibilité, mais dans l'ensemble, c'est divertissant.", "rating": 3},
    {"content": "Le personnage principal est très attachant, ce qui rend le film mémorable.", "rating": 4},
    {"content": "Une approche novatrice de la réalisation qui mérite d'être saluée.", "rating": 5},
    {"content": "Les twists dans l'intrigue sont bien exécutés.", "rating": 4},
    {"content": "Un film qui suscite la réflexion longtemps après la fin.", "rating": 5},
    {"content": "Certains clichés mais une excellente chimie entre les acteurs principaux.", "rating": 3},
    {"content": "L'humour du film est bien dosé et apporte une touche légère.", "rating": 4},
    {"content": "Les effets spéciaux sont parfois exagérés, mais cela ajoute au charme du film.", "rating": 3},
    {"content": "La bande-annonce ne fait pas justice à la qualité réelle du film.", "rating": 4},
    {"content": "Un film qui plaira aux amateurs du genre.", "rating": 4},
    {"content": "Certains moments sont prévisibles, mais l'exécution est impeccable.", "rating": 4},
    {"content": "Un film qui explore des thèmes sociaux importants de manière saisissante.", "rating": 5},

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
    {"content": "Un désastre du genre [ajouter le genre du film].", "rating": 0},
    {"content": "Malheureusement, le film ne parvient pas à captiver l'attention.", "rating": 2},
    {"content": "La trame narrative est confuse et difficile à suivre.", "rating": 1},
    {"content": "Les acteurs semblent peu convaincants dans leurs rôles.", "rating": 2},
    {"content": "Les effets spéciaux laissent à désirer, rendant le film peu crédible.", "rating": 1},
    {"content": "Un scénario prévisible avec des clichés maladroits.", "rating": 2},
    {"content": "La bande sonore est décevante et ne s'aligne pas avec l'ambiance du film.", "rating": 1},
    {"content": "Les dialogues sont plats et manquent d'originalité.", "rating": 2},
    {"content": "L'ensemble du film manque d'émotion et de profondeur.", "rating": 1},
    {"content": "Les personnages ne sont pas bien développés, laissant le spectateur indifférent.", "rating": 2},
    {"content": "Les décors semblent artificiels, nuisant à l'immersion.", "rating": 1},
    {"content": "Le rythme du film est trop lent, ce qui rend l'expérience ennuyeuse.", "rating": 2},
    {"content": "Une tentative malheureuse d'apporter de l'originalité à un concept usé.", "rating": 1},
    {"content": "Les twists dans l'intrigue sont prévisibles et décevants.", "rating": 2},
    {"content": "L'ensemble du film manque de cohérence, laissant le spectateur perplexe.", "rating": 1},
    {"content": "Les scènes d'action sont mal chorégraphiées et peu convaincantes.", "rating": 2},
    {"content": "Un film qui semble avoir perdu son identité artistique.", "rating": 1},
    {"content": "La réalisation est bâclée, donnant l'impression d'un projet inachevé.", "rating": 2},
    {"content": "Le film souffre de nombreuses incohérences dans l'intrigue.", "rating": 1},
    {"content": "Les effets spéciaux sont datés et dépassés.", "rating": 2},
    {"content": "Une expérience cinématographique décevante du début à la fin.", "rating": 1}
]

# Liste des cinémas
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
