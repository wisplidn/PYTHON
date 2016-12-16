from urllib.request import urlopen
from bs4 import BeautifulSoup

url="http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt"
textPage = urlopen(url)

print(textPage.read().decode('utf-8'))