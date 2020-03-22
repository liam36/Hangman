class Secret():
    """docstring for Secret."""

    def __init__(self, word):
        self.word = word
        self.guesses = list()

    def isValid(self):
        return self.word.isalpha()

    def guess(self, guess):
        if not guess.isalpha() or len(guess) > 1 or guess in self.guesses:
            return True

        if not self.alreadyGuessed(guess):
            self.guesses.append(guess.lower())
            self.guesses.sort()

        # Correct guess?
        return guess.lower() in self.word.lower()

    def alreadyGuessed(self, guess):
        return guess.lower() in self.guesses

    def isKnown(self):
        for char in self.word:
            if char.lower() not in self.guesses:
                return False
        return True

    def draw(self):
        s = ""
        wrong = ""

        # build the currently known word string
        for char in self.word:
            if char.lower() in self.guesses:
                if char.isupper():
                    s += " " + char.upper()
                else:
                    s += " " + char
            else:
                s += " _"

        # build the string of wrong guesses
        for char in self.guesses:
            if str(char) not in self.word.lower():
                wrong += str(char.upper()) + ", "

        print("The secret word:" + s)
        print("\nWrong guesses:   " + wrong)
