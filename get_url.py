import requests
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

query = 'how old is Subaru in Rezero'

## Google search query results as a Puthon lists of urls
search_result_list = list(search(query,tld="co.in", num=10,stop=3,pause=1))

page = requests.get(search_result_list[index])

tree = html.fromstring(page.content)

soup = BeautifulSoup(page.content, features="lxml")
