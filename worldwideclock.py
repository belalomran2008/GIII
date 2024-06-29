import requests
from bs4 import BeautifulSoup

url = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(url.content, 'html.parser')
article = soup.find_all('article', attrs = { "class" : "product_pod"})
books = []
for i in range(len(article)):
    name = article[i].find('h3').get_text()
    books.append(name)

print(books)

