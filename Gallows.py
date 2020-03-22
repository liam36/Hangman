class Gallows():
    """docstring for Gallows."""

    def __init__(self):
        self.counter = 0

    # draw the hangman
    def draw(self):
        filename = "Stage"
        if self.counter < 10:
            filename += "0"
        elif self.counter > 10:
            print("Error: cannot print gallows, game is already over")
            return
        filename += str(self.counter) + ".txt"

        file = open(filename, mode='r')
        if file.readable():
            print(file.read())
        else:
            print("Error: cannot print gallows, file not readable")
        file.close()

    # increase counter
    def progress(self):
        self.counter += 1

    def isFinished(self):
        if self.counter > 9:
            return True
        else:
            return False
