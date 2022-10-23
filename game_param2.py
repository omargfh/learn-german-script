# :'#######::'##::::'##::::'###::::'########:::'####:'########::'########:::::'###::::'##::::'##:'####:'##::::'##:
# '##.... ##: ###::'###:::'## ##::: ##.... ##::. ##:: ##.... ##: ##.... ##:::'## ##::: ##:::: ##:. ##:: ###::'###:
#  ##:::: ##: ####'####::'##:. ##:: ##:::: ##::: ##:: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##:: ##:: ####'####:
#  ##:::: ##: ## ### ##:'##:::. ##: ########:::: ##:: ########:: ########::'##:::. ##: #########:: ##:: ## ### ##:
#  ##:::: ##: ##. #: ##: #########: ##.. ##::::: ##:: ##.... ##: ##.. ##::: #########: ##.... ##:: ##:: ##. #: ##:
#  ##:::: ##: ##:.:: ##: ##.... ##: ##::. ##:::: ##:: ##:::: ##: ##::. ##:: ##.... ##: ##:::: ##:: ##:: ##:.:: ##:
# . #######:: ##:::: ##: ##:::: ##: ##:::. ##:':####: ########:: ##:::. ##: ##:::: ##: ##:::: ##:'####: ##:::: ##:
# :.......:::..:::::..::..:::::..::..:::::..::....::........:::..:::::..::..:::::..::..:::::..::....::..:::::..::

import csv
from os import makedirs
import re
from responses import fetcher
from random import randint

class Game(object):
    def __init__(self, f, score_increment=10, allowed_attempts=2):
        self.learned = 0
        self.attempts = 0
        self.score = 0
        self.accuracy = str()

        self.score_increment = score_increment

        self.data = self.load_data(f)
        self.mistakes = list()

        # Dynamic data, changes each round
        self.current_word = dict()
        self.wrong_count = 0
        self.allowed_attempts = allowed_attempts

        # Game stop value
        self.STOP = False

    # Loads all files into the object
    def load_data(self, f):
        with open(f, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            return [{**{"gID": i}, **word} for i, word in enumerate(reader)]

    # Fetch random word
    def fetch_random_word(self, start=0):
        return self.data[randint(start, len(self.data)-1)]

    # Controls the counter for the wrong attempts per game round
    def increment_wrong_count(self):
        if self.wrong_count < self.allowed_attempts:
            self.wrong_count += 1
        else:
            raise("Maximum value exceeded for variable.")

    def reset_wrong_count(self):
        self.wrong_count = 0

    # Round of game, takes in three inputs:
    # the original word, the required input, and the display phrase
    def run_round(self, word, guess, phrase):
        user_guess = input(f"What is the {phrase} {word}? ")
        if user_guess == 'quit':
            self.quit()
            self.check_game_end()
        if user_guess.strip().lower() == guess.lower():
            self.log_correct(word)
        elif self.wrong_count != self.allowed_attempts - 1:
            self.log_wrong()
            self.run_round(word, guess, phrase)
        else:
            self.give_feedback("wrong", guess.lower().capitalize())
            self.attempts += 1
            self.reset_wrong_count()
        self.check_game_end()

    # Print responses to users actions
    def give_feedback(self, state, *args):
        if state == "correct":
            response = f"Amazing. You have learned {self.learned} words so far." if self.learned % 10 == 0 else fetcher.correct()
        elif state == "try again":
            response = fetcher.try_again()
        else:
            response = f"The right answer is {args[0]}."
        print(response)

    # Log correct answerr
    def log_correct(self, word):
        self.learned += 1
        self.attempts += 1
        self.score += 10
        self.data.remove(self.current_word)
        self.update_efficiency()
        self.reset_wrong_count()
        self.give_feedback("correct")

    # Deduct score from player
    def log_wrong(self):
        self.attempts = self.attempts + 1
        self.score = self.score - 5 if self.score > 5 else 0
        self.update_efficiency()
        self.give_feedback("try again")
        self.mistakes.append(self.current_word)
        self.increment_wrong_count()

    # Update efficiency value
    def update_efficiency(self):
        if self.attempts != 0:
            self.accuracy = "{:.2f}%".format(self.learned / self.attempts * 100)

    def log(self, template="template.txt"):
        with open(template, "r") as f:
            content = f.read()
            print()
            replacements = {"\{\{learned\}\}": self.learned,
                            "\{\{attempts\}\}":self.attempts,
                            "\{\{score\}\}": self.score,
                            "\{\{accuracy\}\}": self.accuracy,
                            "\{\{mistakes\}\}": re.sub(",None", "", "\n".join([",".join(items) for items in [list([str(v) for (k,v) in mistake.items()]) for mistake in self.mistakes]]))}
            for key, value in replacements.items():
                content = re.sub(key, str(value), content)
            return content.replace(",None", "")

    # Stops game at last value
    def check_game_end(self):
        with open("logs.txt", "w") as f:
                f.write(self.log())
        if len(self.data) == 0:
            print(f"You learned a total of {self.learned} words with an accuracy of {self.accuracy} and score of {self.score}. See logs.txt for further statistics and a history of your mistakes.")
            self.STOP = True
            exit()

    def quit(self):
        self.STOP = True
        self.data = list()
        self.wrong_count = 2
        self.check_game_end()
