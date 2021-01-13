from tkinter import *
import random
import pandas
import json
#---------------------------------------
# IMPORTED TABLE DATA

data = pandas.read_csv("./data/spanish_words.csv")
df = pandas.DataFrame(data)
pairings = df.to_dict(orient='records')

revision_list = []
known_words =[]

class Card():
    def __init__(self):
        self.score = 0
        self.tries = 0
        self.spanish = pairings[0]['Spanish']
        self.english = pairings[0]['English']
        self.difficulty = "easy"

    def next_card(self):
        self.spanish = pairings[self.tries]['Spanish']
        self.english = pairings[self.tries]['English']

    # # def medium(self):
    #     self.spanish = random.choice(pairings)
    #     self.english = random.choice(pairings)

    def remember(self):
        known_words.append({'Spanish':self.spanish,'English':self.english})
        self.tries += 1
        self.score_update()
        return True

    def forgot(self):
        revision_list.append({'Spanish':self.spanish, 'English':self.english})
        self.tries += 1
        return True

    def score_update(self):
        self.score += 1
        new_data = {'revision':revision_list, 'score': self.score, 'tries':self.tries,'known_words':known_words}
        try:
            with open(f"./scoretracker.json", mode="r") as scoretracker:
                data = json.load(scoretracker)
                data.update(new_data)
                # Reads old data

        except FileNotFoundError:
            with open(f"./passwordlist.json", mode="w") as scoretracker:
                json.dump(new_data, scoretracker, indent=4)

        else:
            print("Something")
            with open(f"./passwordlist.json", mode="w") as scoretracker:
                json.dump(data, scoretracker, indent=4)