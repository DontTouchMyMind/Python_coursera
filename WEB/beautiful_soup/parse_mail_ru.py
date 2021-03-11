from bs4 import BeautifulSoup
import requests


result = requests.get('https://news.mail.ru/')
html = result.text
soup = BeautifulSoup(html, 'lxml')

res = [
    (
        section.string,
        [
            link.string for link in section.find_parents()[4].find_all('span', 'link__text')
        ]
    )for section in soup.find_all('span', 'hdr__inner')
]

for r in res:
    print(r)
