try:
    from re import sub
except ModuleNotFoundError:
    print("Bummer. The nessacary modules cannot be found. If you report this bug, the error code is ModuleNotFoundError.")
# create variables
regex = r'[^A-Za-z0-9 ]+'
email = sub(regex, r'', open("./Email.txt", 'r')).lower().split(r' ')
spam_words = sub(regex, r'', open("./Spam.txt", 'r')).lower().split(r' ')
threshold = len(email)/2
spam_rating = 0

# the acctual code
# for every word in the email
for word in email:
    # see if said word is one of the spam words
    if word in spam_words:
        # and if it is, increase `spam_rating` by 1
        spam_rating += 1
# if the rating is greater than or equal to the threshold, say it is spam, if it is not, say it is not spam
if spam_rating >= threshold:
    print("This is spam!")
else:
    print("This is not spam!")
