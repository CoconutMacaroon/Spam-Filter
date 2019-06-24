from re import sub

email = sub(r'[^A-Za-z0-9 ]+', r'', open("./Email.txt", 'r')).lower().split(r' ')
spam_words = sub(r'[^A-Za-z0-9 ]+', r'', open("./Spam.txt", 'r')).lower().split(r' ')
threshold = len(email)/2
spam_rating = 0  # the lower the less likely is spam!
for word in email:
    if word in spam_words:
        spam_rating += 1
if spam_rating >= threshold:
    print("This is spam!")
else:
    print("This is not spam!")
