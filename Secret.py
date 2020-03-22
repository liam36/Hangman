class Secret():
    """docstring for Secret."""

    def __init__(self, word):
        self.word = word
        self.guesses = list()

    def isValid(self):
        return self.word.isalpha()

    def guess(self, guess):
        if not self.alreadyGuessed(guess):
            self.guesses.append(guess.lower())
        return guess.lower() in self.word

    def alreadyGuessed(self, guess):
        return guess.lower() in self.guesses

    def isKnown(self):
        for char in self.word:
            if char not in self.guesses:
                return False
        return True

    def draw(self):
        s = ""
        for char in self.word:
            if char in self.guesses:
                s += char + " "
            else:
                s += "_ "
        print(s)
