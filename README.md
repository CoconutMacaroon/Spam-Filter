![alt text](https://img.shields.io/badge/license-Unlicense-green.svg "License: Unlicense")
![alt text](https://img.shields.io/github/languages/top/CoconutMacaroon/Spam-Filter.svg "Language: Python")
![alt text](https://img.shields.io/github/issues-raw/CoconutMacaroon/Spam-Filter.svg "Issues")
# Spam Filter
This Python 3 code detects and filters spam. The email in question goes into the `static/Email.txt` file, and then when the program is ran, it prints whether or not it thinks the email is spam.
# Future
* Email program intigration
* Better documentation
* Process `email.txt` and `spam.txt` at the same time to improve performence
# Files
The `Email.txt` and the `Spam.txt` are both in the `static` folder. The file that acctually does the processing and gives the result is `main.py` and is in the home folder.
# How it works
_Full code documentation is in the file `main.py`._  
`main.py` reads the email file, removes all special characters from it (specifically ones that aren't letters, numbers, or spaces), and puts it in an array by spliting it with space as the delimater. It then does the same for `spam.txt`. After both files are processed, it gets the ammount of words for the spam file and the email, and compares the two. If the ammount of spam words in the email is bigger than half the total number of words in the email, it flags it as spam.
# Issues
Found a bug? Let us know in the issues tab and clicking _New issue_.
