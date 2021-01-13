from tkinter import *
import random
import pandas
import json
#---------------------------------------
# IMPORTED TABLE DATA

data = pandas.read_csv("./data/spanish_words.csv")
df = pandas.DataFrame(data)
revision_list = df.to_dict(orient='records')

current_card = {}
known_words = []

class Card():
    def __init__(self):
        self.score = 0
        self.tries = 0
        self.spanish = revision_list[0]['Spanish']
        self.english = revision_list[0]['English']
        self.difficulty = "easy"

    def next_card(self):
        self.tries += 1
        current_card = random.choice(revision_list)
        print(current_card)
        self.spanish = current_card['Spanish']
        self.english = current_card['English']
    # # def medium(self):
    #     self.spanish = random.choice(pairings)
    #     self.english = random.choice(pairings)

    def remember(self):
        known_words.append({'Spanish':self.spanish,'English':self.english})
        print(known_words)
        self.score_update()
        self.next_card()
        return True

    def forgot(self):
        revision_list.append({'Spanish':self.spanish, 'English':self.english})
        print(revision_list)
        self.next_card()
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