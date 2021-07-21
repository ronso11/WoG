import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        try:
            user_guess = int(input("Guess a number between 1 to {}\n".format(difficulty)))
            if 1 <= user_guess <= difficulty:
                return user_guess
            else:
                raise ValueError
        except ValueError:
            print("You didn't choose a number between 1 to {}\n".format(difficulty))


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False


def play(difficulty):
    if compare_results(generate_number(difficulty), get_guess_from_user(difficulty)):
        return True
    else:
        return False
