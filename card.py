class Card:

    def __init__(self, questionText = '', answerText=''):
        self.questionText = questionText
        self.answerText = answerText

    def getQuestion(self):
        return self.questionText

    def getAnswer(self):
        return self.answerText

    def editAnswer(self, newAnswer):
        self.answerText = newAnswer

    def editQuestion(self, newQuestion):
        self.questionText = newQuestion

    def __str__(self):
        return f'Question: {self.questionText}. \nAnswer: {self.answerText}'