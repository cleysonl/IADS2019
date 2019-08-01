from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

"""
    This, you should see a list of all article URLs that the Wikipedia article on Kevin Bacon links to.
"""
# html = urlopen('http://www.bbc.co.uk/news')
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

