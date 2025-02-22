import random

word_list = ["LIFE", "KITE", "LITE","GAME","GATE", "POKE", "HYMN",
             "Love", "Life", "Hope", "Time", "Work", "Home", "Fear", "Wind", "Rain", "Snow", "Song",
             "Dark", "Moon", "Star", "Fish", "Ball", "Jump", "Fire", "Food", "Play", "Hate", "Eyes",
             "Mind", "Hand", "Gold", "Rose", "Tree", "Bird", "Book", "Door", "Road", "Hill", "Hair",
             "Head", "Face", "Word", "Boat", "Ship", "Desk", "Lamp", "Hope", "Wind", "Bear", "Lion",
             "King", "Queen", "Frog", "Deer", "Duck", "Game", "Gift", "Sock", "Shoe", "Sand", "Milk",
             "Star", "Cake", "Desk", "Horn", "Duck", "Moon", "Boot", "Ring", "Hand", "Foot", "Nose",
             "Coat", "Suit", "Sign", "Shop", "Bank", "Work", "Love", "Life", "Moon", "Mars", "Snow",
             "Rain", "Wind", "Fire", "Bird", "Duck", "Rose", "Lily", "Hand", "Head", "Door", "Wall",
             "Tree", "Hill", "Gold", "Book", "Lamp", "Song", "Word", "Time", "Hope", "Fear", "Hate",
             "Play","brisk", "jumps", "glove", "quilt", "vexil", "whorl", "zesty", "charm", "flint", "jokey",
             "hazel", "prick", "snout", "tramp", "vigor", "waltz", "blitz", "chump", "froze", "glyph",
             "knave", "quash", "roast", "stomp", "ulcer", "vinyl", "wryly", "abject", "blight", "cramps",
             "deluxe", "flinch", "jargon", "morbid", "quench", "sphinx", "tundra", "abrupt", "bright",
             "clamps", "driven", "expert", "fumble", "guitar", "hunger", "injury", "jumble", "kidnap",
             "luxury", "mystic", "nozzle", "outcry", "pistol", "quirky", "refine", "sprint", "turban",
             "unique", "voyage", "wander", "xenial", "yellow", "zephyr", "walnut", "violet", "trophy"]

def random_word_selection():
    selected_word = random.choice(word_list).upper()
    print(selected_word)
    return selected_word