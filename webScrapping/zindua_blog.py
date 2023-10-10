import re, requests
from bs4 import BeautifulSoup
import csv



url = "https://zinduaschool.com/blog/"
response = requests.get(url)
html_content = response.text

content = BeautifulSoup(html_content, 'html.parser')

headings = content.find_all('h2')
time = content.find_all('time')
# for heading in headings:
#     headers = headings
with open('Articles.txt', 'w', newline="") as Articles:
    writer = csv.writer(Articles)
    writer.writerow(['HEADINGS'])
    for heading in headings:
        writer.writerow([heading.text])


pattern = r"^[0-9][-.\s][a-zA-Z][-.\s]\d{4}$"

match = re.findall(pattern,html_content)

if match:
    date = match.group()
    print(date)
else:
    print('No Date Found')