import re
import requests
from bs4 import BeautifulSoup


url = "https://faithfulreads.com/"
response = requests.get(url)
html_content = response.text
scrap = BeautifulSoup(response.content, 'html.parser')


tags = scrap.findAll('a')

for tag in tags:
    print(tag.text)