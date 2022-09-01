import smtplib
import datetime as dt
import random

MY_EMAIL = "skjeggnytt@gmail.com"
MY_PASSWORD = "kjbqfjxnoewsgbto"

now = dt.datetime.now()

day_of_week = now.weekday()
# print(day_of_week)



if day_of_week == 2:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        random_quote = random.choice(quote_list)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="wendelbo@gmail.com",
            msg=f"Subject: Motivational Quote!\n\n{random_quote}"
    )


