from Game import Game

game = Game(str(input("Enter a secret: ")))

if not game.hasValidSecret():
    while not game.hasValidSecret():
        game = Game(str(input("Enter a secret made up of letters only: ")))

print("\n" * 100)

while not game.isLost():
    game.guessSecret(input("Guess a letter: "))
    if game.isWon():
        break
