##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import datetime as dt
import pandas as pd
import glob, random



# birthday df CSV
df = pd.read_csv('birthdays.csv')
bdays = df.values.tolist()
# print(bdays)



# letters
letters = []
for letter in glob.glob('letter_templates/*.txt'):
    with open(letter) as f:
        letters.append(f.readlines())
# print(letters)



# datetime
now = dt.datetime.now()
for i in bdays:
    name = i[0]
    email = i[1]
    year = i[2]
    months = i[3]
    day = i[4]
    
    bday = dt.datetime(year=now.year, month=months, day=day)

    if now.month == bday.month and now.day == bday.day:
        # print(f'Happy birthday {name}!')
        print(random.choice(letters))


