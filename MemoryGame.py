import random
import time


def generate_sequence(difficulty):
    random_list = []
    for i in range(0, difficulty):
        random_list.append(random.randint(1, 101))
    print(random_list, end="")
    time.sleep(0.7)
    print("\r  ")
    return random_list


def get_list_from_user(difficulty):
    order = {1: "first", 2: "second", 3: "third", 4: "forth", 5: "fifth"}
    user_list = []
    while True:
        try:
            for i in range(0, difficulty):
                user_input = int(input("please pick the " + order[i + 1] + " number\n"))
                if 1 <= user_input <= 101:
                    int(user_input)
                    user_list.append(user_input)
                else:
                    raise ValueError
            break
        except ValueError:
            print("You should pick a number between 1 to 101")
    return user_list


def is_list_equal(random_list, user_list):
    if sorted(random_list) == sorted(user_list):
        return True
    else:
        return False


def play(difficulty):
    if is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty)):
        return True
    else:
        return False





