import requests
from bs4 import BeautifulSoup
import smtplib
import time

# the url u want to follow
URL = 'https://www.emag.ro/server-intel-server-chassis-r2000wtxxx/pd/DLJJZVBBM/'

# user agent : type in google 'my user agent' and you'll get your user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}


def check_price():
    # store all the data from the URL
    page = requests.get(URL, headers=headers)

    # parse everything
    soup = BeautifulSoup(page.content, 'html.parser')

    # search into the data for the class 'page-title' because if we inspect element our page, the title of the product
    # is found into the class 'page-title'. Get the text from our class using .get_text()
    title = soup.find(attrs={'page-title'}).get_text()

    # extract the price from our page. The problem is that we get the price as a string and we want to compare it
    # to a price we set
    price = soup.find(attrs={'product-highlight product-page-pricing', 'product-new-price'}).get_text()

    # extract the first 5 characters from our price, first we need to strip it and afterwards,
    # select the first 5 characters
    character_price = price.strip()[0:5]

    # delete the ',' character
    character_price = character_price[:1] + character_price[2:]

    # convert the price so we can compare it to our desired price
    converted_price = int(character_price[0:4])

    print(converted_price)

    # ignore all the blank lines using .strip
    print(title.strip())

    if converted_price < 1000:
        send_mail()


def send_mail():
    # establish a connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # password generated with app passwords from google
    server.login('your gmail here', 'your password here')

    subject = 'Price update'
    body = 'Check the link : ' \
           'https://www.emag.ro/server-intel-server-chassis-r2000wtxxx/pd/DLJJZVBBM/'
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('from : ',
                    'to : ',
                    msg)
    print('Mail sent!')
    server.quit()


# check the price once a day
while True:
    check_price()
    time.sleep(60 * 60 * 24)
