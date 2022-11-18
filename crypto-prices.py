import requests
from bs4 import BeautifulSoup

def get_btc_price():
    print("the current prices of digital currency is : ")
    url = requests.get("https://www.coindesk.com/tag/api/")
    contenti = url.content
    soup = BeautifulSoup(contenti, 'html.parser')
    # print(soup.prettify())
    print(type(soup))
    for i, tag in enumerate(soup.find_all('div', attrs={'class': "prices-stripstyles__PricingItemWrapper-sc-19jxxl9-1 fLGzVy"})):
        print(str(i) + ' :' + "Name of cryptocurrency:" + str(tag.span.text) + ", price:" + str(tag.div.text))

if __name__ == '__main__':
    get_btc_price()

