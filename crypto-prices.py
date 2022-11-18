import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import ssl
import smtplib

def get_btc_price():
    print("the current prices of digital currency is : ")
    url = requests.get("https://www.coindesk.com/tag/api/")
    contenti = url.content
    soup = BeautifulSoup(contenti, 'html.parser')
    # print(soup.prettify())
    result ="the current prices of digital currency is : "
    for i, tag in enumerate(soup.find_all('div', attrs={'class': "prices-stripstyles__PricingItemWrapper-sc-19jxxl9-1 fLGzVy"})):
        result += ("\n"+str(i) + ' :' + "Name of Cryptocurrency:" + str(tag.span.text) + ", Price and Fluctuation: " + str(tag.div.text))

    return result


def send_email(body , email_reciever):
    #enter your email here
    email_sender = ""
    #enter password here of sender email
    email_password = ""
    #enter the reciever email here
    email_reciever = ""

    # setting the header of the email
    subject ="Today's Crypto Prices"
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciever
    em["subject"] = subject
    em.set_content(body)

    #security using ssl encryption
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())


if __name__ == '__main__':
    body = get_btc_price()
    email_reciever = ""
    send_email(body=body ,email_reciever="")

