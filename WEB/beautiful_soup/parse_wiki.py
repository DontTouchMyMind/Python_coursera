import re
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://wikipedia.org/')
html = resp.text


def parse_with_re():
    result = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
    print(result)


def parse_with_bs4():
    soup = BeautifulSoup(html, 'lxml')
    result = [tag['href'] for tag in soup('a', 'other-project-link')]
    print(result)


if __name__ == '__main__':
    parse_with_bs4()
    parse_with_re()