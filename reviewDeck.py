from collections import defaultdict, namedtuple
from card import Card


class ReviewDeck:

    def __init__(self, name):
        self.name = name
        self.reviewDeck = dict()

    def addToReviewDeck(self, ques, ans):
        self.reviewDeck[Card(ques, ans)] = [0,0,0]

    def update(self, ques, right=False):
        for k, v in self.reviewDeck.items():
            if k.getQuestion() == ques:
                self.reviewDeck[k][0] += 1
                if right:
                    self.reviewDeck[k][1] += 1
                else:
                    self.reviewDeck[k][2] += 1


    def viewDeck(self):
        print(f'\nVIEWING DECK..........{self.name}')
        for card, reviews in sorted(self.reviewDeck.items(), key=lambda t: t[1]):
            print(f'{card} \n REVIEWED: {reviews}\n----------------')

    def __repr__(self):
        return self.name
