"""
import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name1 = 'my_table_1'
new_field = 'my_1st_column'
field_type = 'INTEGER'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf = new_field, ft = field_type))

conn.commit()
conn.close()
c = conn.cursor()

try:
    c.execute('INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, "test")'
              .format(tn=table_name,idf=id_column,cn=column_name))
except c.IntegrityError()
"""

from collections import defaultdict, namedtuple
reviewData = namedtuple('ReviewData', 'TotalReviews TotalCorrect TotalIncorrect')


class Card:

    def __init__(self, questionText = '', answerText=''):
        self.questionText = questionText
        self.answerText = answerText

    def editAnswer(self, newAnswer):
        self.answerText = newAnswer

    def editQuestion(self, newQuestion):
        self.questionText = newQuestion

    def __str__(self):
        return f'Question: {self.questionText}. \nAnswer: {self.answerText}'


class ReviewDeck:

    def __init__(self, name):
        self.name = name
        self.reviewDeck = defaultdict(reviewData)

    def addToReviewDeck(self, ques, ans):
        self.reviewDeck[Card(ques, ans)] = reviewData(0, 0, 0)

    def viewDeck(self):
        print(f'\nVIEWING DECK..........{self.name}')
        for card, reviews in sorted(self.reviewDeck.items(), key=lambda t: t[1]):
            print(f'{card} \n REVIEWED: {reviews}\n----------------')

    def __repr__(self):
        return self.name


class OpenMenu:

    def __init__(self):
        self.allDecks = set()
        while True:
            option = input('Do you want to review (press R) or create a deck (press C)? ')

            while not (option == 'R' or option == 'C'):
                print('Invalid input')
                option = input('Do you want to review (press R) or create a deck (press C)? ')

            if option == 'R':
                self.review()
                ## How to select which deck?
                ## Support multiple decks?
            if option == 'C':
                self.create()

    def review(self):
        pass

    def create(self):
        name = input('Enter the name of this deck: ')
        review = ReviewDeck(name)
        self.allDecks.add(review)
        while True:
            question = input('Enter the card question, enter DONE to quit: ')
            if question == 'DONE':
                decision = input('Would you like to view current deck? Press Y to view, N to return to main menu ')
                if decision == 'Y':
                    review.viewDeck()
                elif decision == 'N':
                    print('Exiting...\n')
                    return
                else:
                    print('Failed input...Continuing...')
            else:
                answer = input('Enter the card answer: ')
            try:
                review.addToReviewDeck(question, answer)
                print(f'...QUESTION SUCCESFULLY CREATED...')
            except Exception as e:
                print(f'Encountered following error: {e}')

OpenMenu()
