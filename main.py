import datetime as dt
import pandas as pd
import glob, random, smtplib


sender = input('Sender name, email, and email password [ex: John john@gmail.com 1234login]: ').split()
sender_name = sender[0]
sender_email = sender[1]
sender_password = sender[2]


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
    recipient_name = i[0]
    recipient_email = i[1]
    year = i[2]
    month = i[3]
    day = i[4]
    
    bday = dt.datetime(year=now.year, month=month, day=day)

    if now.month == bday.month and now.day == bday.day:
        # print(f'Happy birthday {ecipient}!')
        random_letter = random.choice(letters)
        letter_to_str = ''.join(random_letter)
        
        letter = letter_to_str.replace('[RECIPIENT]', recipient_name).replace('[SENDER]', sender_name)
        # print(letter)


        # Send email
        smtp_server = 'smtp.gmail.com'
        port_number = 587
        
        if '@gmx.com' in recipient_email:
            smtp_server = 'smtp.gmx.com'
            port_number = 587
        elif '@gmail.com' in recipient_email:
            smtp_server = 'smtp.gmail.com'
            port_number = 587
        elif '@hotmail.com' in recipient_email:
            smtp_server = 'smtp.live.com'
            port_number = 587
        elif '@outlook.com' in recipient_email:
            smtp_server = 'outlook.office365.com'
            port_number = 25
        elif '@yahoo.com' in recipient_email:
            smtp_server = 'smtp.mail.yahoo.com'
            port_number = 465
        
        try:
            with smtplib.SMTP(smtp_server, port=port_number) as connection:
                connection.starttls()
                connection.login(user=sender_email, password=sender_password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addr=recipient_email,
                    msg=' '.join([
                        f'From: {sender_name}',
                        f'To: {recipient_email}',
                        f'Subject: 🥳🎂 Happy Birthday 🎈 {recipient_name}🎉🎁',
                        '',
                        f'{letter}'
                    ]).encode('utf-8').strip() # may not need .encode('utf-8').strip()
                )
        except Exception as error:
            print(f'Error: {error}')