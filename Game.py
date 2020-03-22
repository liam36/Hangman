from Secret import Secret
from Gallows import Gallows


class Game():
    """docstring for Game."""

    def __init__(self, secret):
        self.gallows = Gallows()
        self.secret = Secret(secret)

    def draw(self):
        print("\n" * 100)
        print("Hangman\n\n")
        self.gallows.draw()
        print("\n\n")
        self.secret.draw()
        print("\n\n")

    def guessSecret(self, guess):
        if self.secret.guess(guess):
            print("Correct!")
        else:
            self.gallows.progress()
        self.draw()

    def isLost(self):
        return self.gallows.isFinished()

    def isWon(self):
        return self.secret.isKnown()

    def hasValidSecret(self):
        return self.secret.isValid()
