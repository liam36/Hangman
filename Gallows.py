class Gallows():
    """docstring for Gallows."""

    def __init__(self):
        super(Gallows, self).__init__()
        self.progress = 0

    def print(self):
        filename = "Stage"
        if self.progress < 10:
            filename += " "
        filename += str(self.progress) + ".txt"

        file = open(filename, mode='r')
        if file.readable():
            print(file.read())
        else:
            print("Error: cannot print gallows")
        file.close()

    def continue(self):
        progress += 1

    def isFinished(self):
        if progress > 9:
            return true
        else:
            return false
