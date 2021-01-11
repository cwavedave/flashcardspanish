import random
import pandas
#---------------------------------------
# IMPORTED TABLE DATA

data = pandas.read_csv("./data/spanish_words.csv")
df = pandas.DataFrame(data)
pairings = df.to_dict(orient='records')
print(pairings[1]['Spanish'])
print(pairings)

class Card():
    def __init__(self):
        self.spanish = self.easy()
        self.score = 0
        self.tries = 0
        self.spanish = pairings[0]['Spanish']
        self.english = pairings[0]['English']

    def easy(self):
        self.spanish = pairings[self.tries]['Spanish']
        self.english = pairings[self.tries]['English']

    def medium(self):
        self.spanish = pairings[random.randint(0,len(pairings))]
        self.english = pairings[random.randint(0,len(pairings))]

    def incorrect(self):
        print("incorrect")

    def correct(self):
        print("correct")

    def next_card(self):
        print("next card")

    def score(self):
        self.score = 0

    def score_update(self):
        self.score += 1

    def tries_counter(self):
        self.tries += 1