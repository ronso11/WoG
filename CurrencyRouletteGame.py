import requests
import random


def gen_random_number():
    ran_number = random.randint(1, 100)
    return ran_number


def get_money_interval():
    response = requests.get('https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=1f578131e3b3c69ba37e')
    return float(response.json()["USD_ILS"])


def get_guess_from_user(random_number):
    while True:
        try:
            user_guess = input("Please guess how much is {} USD in ILS?\n".format(random_number))
            if user_guess.isnumeric():
                return float(user_guess)
            else:
                raise ValueError
        except ValueError:
            print("Wrong input, please try again")


def play(difficulty):
    rand = gen_random_number()
    total_in_ils = rand * get_money_interval()
    interval = (total_in_ils - (5 - difficulty), total_in_ils + (5 - difficulty))
    user_guess = get_guess_from_user(rand)
    if interval[0] <= user_guess <= interval[1]:
        return True
    else:
        return False
