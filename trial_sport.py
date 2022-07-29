import requests
from bs4 import BeautifulSoup as bs
import config
def search(req):
    config.params = {
        'change_price': '',
        'q': req,
        'select_category': '1',
        's': '0',
        'c1': '0',
        'price_from': '0',
        'price_to': '1 100 000',
    }
    response = requests.get('https://trial-sport.ru/gds.php', params=config.params, cookies=config.cookies, headers=config.headers)
    soup = bs(response.text, "lxml")
    price_full = soup.find_all("span", class_="price")
    price_sell = soup.find_all("span", class_="discount")
    image = soup.find_all("a", class_="img__in")
    name = soup.find_all("a", class_="title")
    ids = []
    prices_full = []
    prices_sell = []
    images_ = []
    names = []
    for i in name:
        names.append(i.find('span').text)
        ids.append("https://trial-sport.ru"+i['href'])
    for i in image:
        images = i.find("img")
        images_.append(images["src"])
    for i in price_full:
        price_ = i.find("span", class_="value").text
        prices_full.append(price_.replace("\u2009", " "))
    for i in price_sell:
        price_ = i.find("span", class_="value").text
        prices_sell.append(price_.replace("\u2009", " "))
    list = []
    list.append(prices_full)
    list.append(prices_sell)
    list.append(images_)
    list.append(names)
    list.append(ids)
    return list