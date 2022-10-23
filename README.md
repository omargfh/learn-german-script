# German Quiz Python Script

This is a simple python script to learn german words. It has multiple modes to test your knowledge in vocabulary, articles, and plurals. The game is run in the terminal and is very simple to use. The script keeps track of your score and incorrect words, and they are stored in a log file.

## Installation
1. Clone the repository
2. Install the requirements
3. Run the script

## Usage
```bash
usage: python3 main.py -h -f <file> -m <mode> -e --clear
```

### Arguments
- `-h` : Help
- `-f` : File to read from
- `-m` : Mode to run the game in (translation, artikel, plural)
- `-e` : Export categories/articles to separate files
- `--clear` : Clear the export directory before exporting

### Commands
- `quit` : Quit the game (may be used at any time)

### Examples
1. Initial run, start of round
```bash
$ python3 main.py -f words.txt -m artikel
What is the article of anschluss?
```

2. Correct answer
```bash
$ python3 main.py -f words.txt -m artikel
What is the article of anschluss? der
You're doing great.

What is the article of guertel?
```

3. Incorrect attempt
```bash
$ python3 main.py -f words.txt -m artikel
What is the article of guertel? das
Hey, don't feel down. Try again.
What is the article of guertel?
```

4. Two incorrect attempts
```bash
$ python3 main.py -f words.txt -m artikel
What is the article of termin? das
You should have another guess at this.
What is the article of termin? die
The right answer is Der.
```

5. End of Game
```bash
$ python3 main.py -f words.txt -m artikel
You learned a total of 2 words with an accuracy of 100.00% and score of 20. See logs.txt for further statistics and a history of your mistakes.
```

6. Exporting categories/articles
```bash
Exporting categories and articles to files...
Done.
```

## Modes
### Translation (uebersetzung)
The user is given an English word and must provide the German translation. The user is given 2 attempts to guess the correct answer. On the second mistake, the word is skipped and the correct answer is given to the user. The word is then added to the log file as a mistake and is reviewed later by the script.

### Artikel
The user is given a German word and must provide the correct article. The user is given 2 attempts to guess the correct answer. On the second mistake, the word is skipped and the correct answer is given to the user. The word is then added to the log file as a mistake and is reviewed later by the script.

### Plural
The user is given a German word and must provide the correct plural form. The user is given 2 attempts to guess the correct answer. On the second mistake, the word is skipped and the correct answer is given to the user. The word is then added to the log file as a mistake and is reviewed later by the script.

## Log File
The log file is a simple text file that contains the words that the user has missed. The file is formatted as follows:
```bash
Words learned: <number>
Total attempts made: <number>
Score: <number>
Accuracy: <number>

id,<csv_entry>
```

The csv entry is formatted as the input CSV file. The id is a unique identifier for the word. The id is used to keep track of the words that the user has missed. The id is incremented by 1 for each word in the CSV.

## Input CSV File
The input CSV file is a simple text file that contains the words that the user wants to learn. The file must contain the `wort` column. Otherwise, it must satisfy different requirements depending on the mode that the user is running the game in.

### Translation
The input CSV file must contain the `uebersetzung` column. This column holds the English translation for a given German word stored in `wort`.

### Artikel
The input CSV file must contain the `artikel` column. This column holds the correct article for a given German word stored in `wort`.

### Plural
The input CSV file must contain the `plural` column. This column holds the correct plural form for a given German word stored in `wort`.

### Export Columns

#### `kategorie` column
The `kategorie` column holds the category for a given word. This column is used to group words together. The user can use the `-e` flag to export the words to separate files based on their category. This is mandatory if for `export`.

#### `sekundaer_kategorie`
The `sekundaer_kategorie` column holding the secondary category for a given word. This column is used to group words together. The user can use the `-e` flag to export the words to separate files based on their secondary category. This is mandatory if for `export`.

#### `artikel` column
The `artikel` column holds the correct article for a given German word stored in `wort`. This column is used to  This is mandatory if for `export`.

#### Optional Columns
The following columns are optional and are not used by the script. They are used to provide additional information about the word.
- `alt` : Alternate English translation of the German word stored in `wort`.

## Export
The user can use the `-e` flag to export the words to separate files based on their category. The user must provide the `kategorie` and `artikel` columns in the input CSV file. The user can also provide the `sekundaer_kategorie` column to further group the words. The script will create two directory called `categories/` and `artikel/` in the `./export` directory. The script will create a `csv` file for every category and subcategory. The script will create a file for each article. The file will contain the words that belong to that category, secondary category, and article. The file will be named `[kategorie|sekundaer_kategorie|artikel].csv`. The file will be formatted as the input CSV file.

### Behavior Notes
Default behavior is to append current files. Use the `--clear` flag to clear the export directory before exporting.

### Mandatory Columns
- `wort` : German word
- `artikel` : Article of the word
- `kategorie` : Category of the word
- `sekundaer_kategorie` : Secondary category of the word

### Optional Columns (appear in the output)
- `uebersetzung` : English translation of the word
- `plural` : Plural form of the word
- `alt` : Alternate English translation of the word

### Example
```bash
$ python3 main.py -f words.csv -e
```

## Scoring
Correct answers increment score by 10. Incorrect answers decrement score by 5. The score is capped at 0. The score is displayed at the end of the game.

## Challenges with Unicode
The script assumes `utf-8` encoding for the use of umlauts. However, provided CSV files designate umlauts with an extra `e` next to the regular version of the character. Similarly, Eszett is `ss`.

### Example
- `ä` : `ae`
- `ö` : `oe`
- `ü` : `ue`
- `ß` : `ss`

## Provided CSV Files
The script comes with a few CSV files that can be used to test the script. The files are located in the `./csv` directory. The files include:
- `data.csv` : Contains a list of German non-verb words in different categories and articles (count: 714)
- `verben.csv` : Contains a list of German verbs in different categories (count: 149)
- `verschiedenes.csv` : Contains a list of German miscellaneous entries (count: <100)

Export examples are also provided.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Authors
- [**Omar Ibrahim**](github.com/omargfh)

## Acknowledgements
- [**dict.cc API**](https://github.com/rbaron/dict.cc.py)

## Disclaimer
This project is for educational purposes only. It is not intended to be used in real life scenarios.

## Future Work
- [ ] Implement Unicode character conversions
- [ ] Fix bugs

## Changelog
- 0.1.0
    - Initial release

## Meta
Omar Ibrahim – [@omaribb_](https://instagram.com/omaribb_) – [www.omar-ibrahim.com](https://www.omar-ibrahim.com)

Distributed under the MIT license. See ``LICENSE`` for more information.