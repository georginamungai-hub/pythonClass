import csv
import requests
from bs4 import BeautifulSoup

url = 'https://hojaleaks.com'
response = requests.get(url)

print(response)
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

headings = soup.find_all('h1')

for heading in headings:
    print(heading.text)

with open ('headings.txt', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['HEADINGS'])
    for heading in headings:
        writer.writerow([heading.text])
