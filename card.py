from tkinter import *
import random
import pandas
import json
#---------------------------------------
# IMPORTED TABLE DATA

data = pandas.read_csv("./data/spanish_words.csv")
df = pandas.DataFrame(data)
new_words = df.to_dict(orient='records')

new_data = pandas.read_json("./data/scoretrack.json",typ="series")
df_new_data = pandas.DataFrame(new_data)

revision_list = df_new_data.to_dict(orient='records')


current_card = {}
known_words = []

class Card():
    def __init__(self):
        self.score = 0
        self.tries = 0
        self.spanish = new_words[0]['Spanish']
        self.english = new_words[0]['English']
        self.difficulty = "easy"

    def next_card(self,result):
        self.tries += 1
        revision_cards = revision_list[0]
        current_cards = random.choice(revision_cards)
        current_card = random.choice(current_cards)
        print(f"current card = {current_card['Spanish']}")
        if result == True:
            new_words.remove(current_card)
            print("Remembered")
        elif result == False:
            print("Forgot")

        self.spanish = current_card["Spanish"]
        self.english = current_card["English"]
    # # def medium(self):
    #     self.spanish = random.choice(pairings)
    #     self.english = random.choice(pairings)

    def remember(self):
        known_words.append({'Spanish':self.spanish,'English':self.english})
        self.score_update()
        self.next_card(True)
        return True

    def forgot(self):
        new_words.append({'Spanish':self.spanish,'English':self.english})
        print(new_words)
        self.next_card(False)
        return True

    def score_update(self):
        self.score += 1
        new_data = {'revision':new_words, 'score': self.score, 'tries':self.tries, 'known_words':known_words}
        try:
            with open(f"./data/scoretrack.json", mode="r") as scoretracker:
                data = json.load(scoretracker)
                data.update(new_data)
                # Reads old data

        except FileNotFoundError:
            with open(f"./data/scoretrack.json", mode="w") as scoretracker:
                json.dump(new_data, scoretracker, indent=4)

        else:
            with open(f"./data/scoretrack.json", mode="w") as scoretracker:
                json.dump(data, scoretracker, indent=4)