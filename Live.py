from GuessGame import play as play_guessing_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_currency_roulette

games = {1: "'Memory Game'", 2: "'Guess Game'", 3: "'Currency Roulette'"}


def get_game():
    game = input("Please Choose a game to play:\n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have "
                 "to guess it back\n"
                 "2. Guess Game - guess a number and see if you chose like the computer.\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    return game


def welcome(name: str) -> str:
    greeting = "Hello" + " " + name + " " + "and welcome to the World of Games(WoG).\n" \
                                            "Here you can find many cool games to play\n"

    return greeting


def difficulty_level():
    while True:
        try:
            difficulty = input("Please choose game difficulty from 1 to 5:\n")
            if validate(difficulty, range(1, 6)):
                return int(difficulty)
            else:
                raise ValueError
        except ValueError:
            print("Difficulty level doesn't exist.")


def validate(user_input, values):
    if user_input.isnumeric():
        if int(user_input) in values:
            return True
        else:
            return False
    else:
        return False


def choose_games():
    while True:
        try:
            play_game = get_game()
            if validate(play_game, range(1, 4)):
                return int(play_game)
            else:
                raise ValueError
        except ValueError:
            print("Game Doesn't exist, please choose a game between 1 and 3")


def load_game():
    game = choose_games()
    difficulty = difficulty_level()
    print("You choose to play" + " " + games[game] + " " + "Difficulty level: {}".format(difficulty))
    print("*" * 80)
    result = None
    if game == 1:
        result = play_memory_game(difficulty)
    elif game == 2:
        result = play_guessing_game(difficulty)
    elif game == 3:
        result = play_currency_roulette(difficulty)

    if result:
        print("You won!!!")
    else:
        print("You lose, better luck next time")