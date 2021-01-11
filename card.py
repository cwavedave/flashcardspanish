import random
import pandas
#---------------------------------------
# IMPORTED TABLE DATA

data = pandas.read_csv("./data/spanish_words.csv")
df = pandas.DataFrame(data)
pairings = df.to_dict(orient='records')
# print(pairings[1]['Spanish'])
# print(pairings)


class Card():
    def __init__(self):
        self.spanish = self.easy()
        self.score = 1
        self.tries = 1
        self.spanish = pairings[0]['Spanish']
        self.english = pairings[0]['English']
        self.difficulty = "easy"

    def easy(self):
        self.spanish = pairings[self.tries]['Spanish']
        self.english = pairings[self.tries]['English']

    def medium(self):
        self.spanish = pairings[random.randint(0,len(pairings))]
        self.english = pairings[random.randint(0,len(pairings))]

    def correct(self):
        self.tries += 1
        self.score_update()
        self.next_card()

    def incorrect(self):
        self.tries += 1
        self.english
        self.next_card()

    def next_card(self):
        if self.difficulty == 'easy':
            self.easy()
        elif self.difficulty == 'medium':
            self.medium()

    def score_update(self):
        self.score += 1
