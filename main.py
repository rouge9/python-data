##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv('birthdays.csv')

birthdata = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows() }
# print(birthdata)
# check if today is a birthday
today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birthdata:
    birthday_person = birthdata[today]
    file_path = f"letter/letter_{random.randint(1,3)}.txt"
    with open(file_path,"r+") as file:
        letter = file.read()
        content = letter.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("robelgedamu92@gmail.com", "rouge12roba")
        connection.sendmail("robelgedamu92@gmail.com", "robelgedamu92@gmail.com",msg=f"Subject: Happy birthday\n\n{content}")