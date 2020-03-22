class Gallows():
    """docstring for Gallows."""

    def __init__(self):
        super(Gallows, self).__init__()
        self.progress = 0

    # draw the hangman
    def printNext(self):
        filename = "Stage"
        if self.progress < 10:
            filename += " "
        elif self.progress > 10:
            print("Error: cannot print gallows, game is already over")
            return
        filename += str(self.progress) + ".txt"

        file = open(filename, mode='r')
        if file.readable():
            print(file.read())
        else:
            print("Error: cannot print gallows, file not readable")
        file.close()

        self.progress += 1

    def isFinished(self):
        if self.progress > 9:
            return true
        else:
            return false
