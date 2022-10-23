# :'#######::'##::::'##::::'###::::'########:::'####:'########::'########:::::'###::::'##::::'##:'####:'##::::'##:
# '##.... ##: ###::'###:::'## ##::: ##.... ##::. ##:: ##.... ##: ##.... ##:::'## ##::: ##:::: ##:. ##:: ###::'###:
#  ##:::: ##: ####'####::'##:. ##:: ##:::: ##::: ##:: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##:: ##:: ####'####:
#  ##:::: ##: ## ### ##:'##:::. ##: ########:::: ##:: ########:: ########::'##:::. ##: #########:: ##:: ## ### ##:
#  ##:::: ##: ##. #: ##: #########: ##.. ##::::: ##:: ##.... ##: ##.. ##::: #########: ##.... ##:: ##:: ##. #: ##:
#  ##:::: ##: ##:.:: ##: ##.... ##: ##::. ##:::: ##:: ##:::: ##: ##::. ##:: ##.... ##: ##:::: ##:: ##:: ##:.:: ##:
# . #######:: ##:::: ##: ##:::: ##: ##:::. ##:':####: ########:: ##:::. ##: ##:::: ##: ##:::: ##:'####: ##:::: ##:
# :.......:::..:::::..::..:::::..::..:::::..::....::........:::..:::::..::..:::::..::..:::::..::....::..:::::..::

from game_param2 import Game
from sys import argv
import argparse
from export_cat import export
# usage: python3 main.py -h -f <file> -m <mode> -e --clear
# default: python3 main.py -f data.csv -m artikel -h

# parse arguments
games = ['artikel', 'translation', 'uebersetzung', 'plural']
parser = argparse.ArgumentParser(description='A simple German vocabulary game.')
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File to load data from", default="data.csv")
parser.add_argument("-m", "--mode", help="Mode to run the game in", default="artikel", choices=games)
parser.add_argument("-e", "--export", help="Export categories and article files into different files", default=False, action="store_true")
parser.add_argument("--clear", help="Clear the export directory before exporting", default=False, action="store_true")
args = parser.parse_args()

if (args.export):
    # call export_cat.py with file
    print("Exporting categories and articles to files...")
    export(args.file, args.clear)
    print("Done.")
    exit()

DATA = args.file
GAME_TYPE = args.mode in games and args.mode or 'artikel'
GAME_TYPE = GAME_TYPE.lower()

game = Game(DATA)
while(not game.STOP):
    game.current_word = game.fetch_random_word()
    if GAME_TYPE == "artikel":
        game.run_round(game.current_word["wort"], game.current_word["artikel"], "article of")
    elif GAME_TYPE == "translation" or GAME_TYPE == "uebersetzung":
        game.run_round(game.current_word["uebersetzung"], game.current_word["wort"], "German word for")
    elif GAME_TYPE == "plural":
        game.run_round(game.current_word["wort"], game.current_word["plural"], "plural of")
    else:
        print("Invalid game type.")
        break