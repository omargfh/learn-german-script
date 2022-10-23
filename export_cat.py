# :'#######::'##::::'##::::'###::::'########:::'####:'########::'########:::::'###::::'##::::'##:'####:'##::::'##:
# '##.... ##: ###::'###:::'## ##::: ##.... ##::. ##:: ##.... ##: ##.... ##:::'## ##::: ##:::: ##:. ##:: ###::'###:
#  ##:::: ##: ####'####::'##:. ##:: ##:::: ##::: ##:: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##:: ##:: ####'####:
#  ##:::: ##: ## ### ##:'##:::. ##: ########:::: ##:: ########:: ########::'##:::. ##: #########:: ##:: ## ### ##:
#  ##:::: ##: ##. #: ##: #########: ##.. ##::::: ##:: ##.... ##: ##.. ##::: #########: ##.... ##:: ##:: ##. #: ##:
#  ##:::: ##: ##:.:: ##: ##.... ##: ##::. ##:::: ##:: ##:::: ##: ##::. ##:: ##.... ##: ##:::: ##:: ##:: ##:.:: ##:
# . #######:: ##:::: ##: ##:::: ##: ##:::. ##:':####: ########:: ##:::. ##: ##:::: ##: ##:::: ##:'####: ##:::: ##:
# :.......:::..:::::..::..:::::..::..:::::..::....::........:::..:::::..::..:::::..::..:::::..::....::..:::::..::

import numpy as np
import pandas as pd
from random import randint
import csv
import re
import os
import sys
from shutil import rmtree

def export(export = "data.csv", clear = False):
    DATA = export
    if (DATA == None):
        DATA = "data.csv"
        print("No file specified, using default file: data.csv")

    if (DATA.split('.')[-1] != 'csv'):
        print("Invalid file type, must be csv.")
        return

    files = set()

    data = pd.read_csv(DATA)

    # mkdirs artikel and cateogires in export folder
    if (clear):
        try:
            rmtree('export')
        except:
            pass

    try:
        os.mkdir("export")
        os.mkdir("export/artikel")
        os.mkdir("export/categories")
    except OSError as error:
        pass

    for index, row in data.iterrows():
        # check row has key artikel
        if (row["artikel"] == None):
            break

        with open(f"export/artikel/{row['artikel']}.csv", "a", encoding="utf-8") as csvfile:
            files.add(f"export/artikel/{row['artikel']}.csv")
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([row['artikel'], row['wort'], row['plural'], row['uebersetzung'], row['kategorie'], row['sekundaer_kategorie'], row['alt']])

    data.dropna(subset = ["kategorie"], inplace=True)
    for index, row in data.iterrows():
        # check row has key kategorie
        if (row["kategorie"] == None):
            break
        with open(f"export/categories/{row['kategorie']}.csv", "a", encoding="utf-8") as csvfile:
            files.add(f"export/categories/{row['kategorie']}.csv")
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([row['artikel'], row['wort'], row['plural'], row['uebersetzung'], row['kategorie'], row['sekundaer_kategorie'], row['alt']])

    def line_prepender(filename, line):
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)

    def clear_lines(filename, delimiter, substitute):
        with open(filename, 'r') as f:
            content = f.readlines()
            for i, line in enumerate(content):
                content[i] = re.sub(delimiter, substitute, content[i])
            with open(filename, 'w') as f_read:
                f_read.writelines(content)


    for file in files:
        line_prepender(file, "artikel,wort,plural,uebersetzung,kategorie,sekundaer_kategorie,alt")
        clear_lines(filename=file, delimiter="^\n", substitute="")
        clear_lines(filename=file, delimiter=",nan", substitute=",")

if __name__ == "__main__":
    main()