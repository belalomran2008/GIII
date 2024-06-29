import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(url.content, 'html.parser')
article = soup.find_all('article', attrs = { "class" : "product_pod"})
# print(article[0])
books = []
prices = []
ratings = []
for i in range(len(article)):
    name = article[i].find('h3').get_text()
    price = article[i].find('p', attrs = { "class" : "price_color"}).get_text()
    rating = article[i].find('p').get('class')[1]
    prices.append(price)
    books.append(name)
    ratings.append(rating)

a = {'name': books,
    'rating': ratings,
    'price': prices}

df = pd.DataFrame(a)
print(df)