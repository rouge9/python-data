import datetime as dt
import smtplib
import random

day = dt.datetime.now()
# current day of the week
day_of_week = day.weekday()
# check if the day of the week sunday
if day_of_week == 5:

    with open("quotes.txt") as data:
        line = data.read().splitlines()
        random_quote = random.choice(line)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="robelgedamu92@gmail.com", password="rouge12roba")
        connection.sendmail(from_addr="robelgedamu92@gmail.com",
                            to_addrs="robelgedamu92@gmail.com",
                            msg=f"Subject: daily Quotes\n\n {random_quote}")
