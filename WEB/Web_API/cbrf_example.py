import requests
from bs4 import BeautifulSoup


resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(resp.content, 'xml')

rate_eur = soup.find('CharCode', text='EUR').find_next_sibling('Value').string  # Поиск по имени
print(f'EUR: {rate_eur} ₽')

rate_eur = soup.find(ID='R01239').Value.string  # Поиск по id
print(f'EUR: {rate_eur} ₽')