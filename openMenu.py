from reviewDeck import ReviewDeck
import random

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
        print(f'...EXISTING DECKS...{self.allDecks}')
        dex = list(self.allDecks)
        print(dex)
        chosen = None
        try:
            deckChoice = int(
                input(f'Which deck do you want to review?. Print the # of Deck, starting from 1 being the first'))
            chosen = dex[deckChoice-1]
        except Exception as e:
            print(f'Exception Occured {e}')
        if not chosen:
            raise AssertionError('No such deck')
        print('Press enter to view answer.')
        while True:
            question = random.choice(list(chosen.reviewDeck.keys()))
            print(f'QUESTION: {question.getQuestion()}')
            if input() is '':
                print(f'ANSWER: {question.getAnswer()}')
            valid = input('Was answer correct or wrong? Enter C or W')
            if valid == 'C':
                chosen.update(question.getQuestion(), True)
            elif valid == 'W':
                chosen.update(question.getQuestion(), False)
            decision = input('Press * to exit and view results.')
            if decision == '*':
                chosen.viewDeck()
                return

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
