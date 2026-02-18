import json
import random

# 10 genres matching your current app
GENRES = [
    (1, "Action"),
    (2, "Comedy"),
    (3, "Drama"),
    (4, "Thriller"),
    (5, "Sci-Fi"),
    (6, "Romance"),
    (7, "Horror"),
    (8, "Animation"),
    (9, "Family"),
    (10, "Crime"),
]

# 200 real movie titles (manually curated list)
TITLES_200 = [
    "The Shawshank Redemption","The Godfather","The Dark Knight","Pulp Fiction","Fight Club",
    "Forrest Gump","Inception","The Matrix","Goodfellas","Se7en",
    "The Silence of the Lambs","Interstellar","The Green Mile","Gladiator","The Departed",
    "Saving Private Ryan","Schindler's List","The Pianist","The Prestige","Whiplash",
    "The Lion King","Toy Story","Finding Nemo","Up","WALL·E",
    "Spirited Away","Princess Mononoke","My Neighbor Totoro","Coco","Inside Out",
    "Titanic","La La Land","The Notebook","Pride & Prejudice","Notting Hill",
    "Pretty Woman","The Terminator","Terminator 2: Judgment Day","Alien","Aliens",
    "Blade Runner","Blade Runner 2049","Mad Max: Fury Road","John Wick","Die Hard",
    "Lethal Weapon","The Bourne Identity","The Bourne Supremacy","The Bourne Ultimatum","Mission: Impossible",
    "Mission: Impossible II","Mission: Impossible III","Ghost Protocol","Rogue Nation","Fallout",
    "The Avengers","Avengers: Infinity War","Avengers: Endgame","Iron Man","Captain America: The Winter Soldier",
    "Guardians of the Galaxy","Spider-Man: Into the Spider-Verse","Spider-Man: Homecoming","Logan","The Batman",
    "Joker","The Usual Suspects","Memento","The Sixth Sense","Shutter Island",
    "The Social Network","The Big Short","Moneyball","The Wolf of Wall Street","Catch Me If You Can",
    "Ocean's Eleven","Ocean's Twelve","Ocean's Thirteen","Heat","Collateral",
    "Casino","Taxi Driver","Raging Bull","A Beautiful Mind","The Imitation Game",
    "Django Unchained","Inglourious Basterds","Once Upon a Time in Hollywood","Reservoir Dogs","Kill Bill: Vol. 1",
    "Kill Bill: Vol. 2","The Hateful Eight","No Country for Old Men","Fargo","The Big Lebowski",
    "The Grand Budapest Hotel","Moonrise Kingdom","Parasite","Oldboy","Memories of Murder",
    "Train to Busan","The Handmaiden","Pan's Labyrinth","The Shape of Water","Children of Men",
    "Gravity","The Martian","Arrival","Ex Machina","Her",
    "Eternal Sunshine of the Spotless Mind","The Truman Show","Groundhog Day","Back to the Future","Back to the Future Part II",
    "Back to the Future Part III","Indiana Jones and the Raiders of the Lost Ark","Indiana Jones and the Last Crusade","Jurassic Park","Jaws",
    "E.T. the Extra-Terrestrial","Close Encounters of the Third Kind","The Goonies","Stand by Me","The Breakfast Club",
    "Ferris Bueller's Day Off","Home Alone","Ghostbusters","Beetlejuice","The Princess Bride",
    "Harry Potter and the Sorcerer's Stone","Harry Potter and the Prisoner of Azkaban","The Lord of the Rings: The Fellowship of the Ring","The Lord of the Rings: The Two Towers","The Lord of the Rings: The Return of the King",
    "The Hobbit: An Unexpected Journey","Star Wars: A New Hope","The Empire Strikes Back","Return of the Jedi","Rogue One: A Star Wars Story",
    "The Force Awakens","The Last Jedi","The Rise of Skywalker","A Quiet Place","Get Out",
    "Us","The Conjuring","The Conjuring 2","It","It Chapter Two",
    "Hereditary","Midsommar","The Shining","Doctor Sleep","Halloween",
    "Scream","The Ring","The Exorcist","The Blair Witch Project","Saw",
    "The Hangover","Superbad","Step Brothers","Anchorman: The Legend of Ron Burgundy","Bridesmaids",
    "Mean Girls","21 Jump Street","22 Jump Street","Zoolander","Dumb and Dumber",
    "Borat","Shaun of the Dead","Hot Fuzz","Scott Pilgrim vs. the World","Knives Out",
    "Glass Onion","The Nice Guys","Baby Driver","Drive","Nightcrawler",
    "The Revenant","Birdman","Argo","Spotlight","12 Years a Slave",
    "The King's Speech","Slumdog Millionaire","The Hurt Locker","Black Swan","The Theory of Everything",
    "The Grandmaster","Ip Man","Crouching Tiger, Hidden Dragon","Hero","House of Flying Daggers",
    "Rocky","Creed","The Karate Kid","Remember the Titans","Friday Night Lights",
    "The Pursuit of Happyness","The Greatest Showman","Les Misérables","The Sound of Music","Mary Poppins",
    "Ratatouille","Monsters, Inc.","The Incredibles","Shrek","Kung Fu Panda",
    "How to Train Your Dragon","Frozen","Moana","Zootopia","The Lego Movie",
    "The Jungle Book","Aladdin","Beauty and the Beast","Mulan","Hercules",
]

def choose_genre_id(title: str) -> int:
    t = title.lower()
    # quick heuristic mapping
    if any(k in t for k in ["star wars","avengers","iron man","captain america","mission: impossible","john wick","die hard","mad max","bourne"]):
        return 1  # Action
    if any(k in t for k in ["hangover","superbad","step brothers","anchorman","bridesmaids","mean girls","zoolander","dumb and dumber","borat"]):
        return 2  # Comedy
    if any(k in t for k in ["conjuring","hereditary","midsommar","shining","exorcist","blair witch","saw","ring","it ","halloween","scream","a quiet place","get out","us"]):
        return 7  # Horror
    if any(k in t for k in ["toy story","finding nemo","up","wall","spirited away","totoro","coco","ratatouille","monsters","incredibles","shrek","kung fu panda","frozen","moana","zootopia","lego"]):
        return 8  # Animation
    if any(k in t for k in ["home alone","jungle book","aladdin","beauty and the beast","mulan","lion king","mary poppins","sound of music"]):
        return 9  # Family
    if any(k in t for k in ["godfather","goodfellas","casino","taxi driver","heat","collateral","departed","joker"]):
        return 10 # Crime
    if any(k in t for k in ["inception","interstellar","matrix","blade runner","alien","martian","arrival","ex machina","gravity","children of men"]):
        return 5  # Sci-Fi
    if any(k in t for k in ["titanic","la la land","notebook","pride","pretty woman","notting hill"]):
        return 6  # Romance
    if any(k in t for k in ["seven","memento","sixth sense","shutter island","nightcrawler","drive","gone"]):
        return 4  # Thriller
    return 3  # Drama default

def main():
    random.seed(42)

    data = []
    # genres
    for pk, name in GENRES:
        data.append({"model": "movies.genre", "pk": pk, "fields": {"name": name}})

    # movies
    pk = 1
    for title in TITLES_200[:200]:
        data.append({
            "model": "movies.movie",
            "pk": pk,
            "fields": {
                "title": title,
                "genre": choose_genre_id(title),
                "release_year": random.randint(1970, 2025),
                "number_in_stock": random.randint(1, 20),
                "daily_rental_rate": f"{random.choice([1.99,2.49,2.99,3.49,3.99,4.49,4.99,5.49,5.99]):.2f}",
            }
        })
        pk += 1

    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
