import requests
import re


URL = 'http://cbr.ru'
result = requests.get(URL)

html = result.text

match = re.search(r'mono-num\D+(\d+,\d+)', html)
rate_usd = match.group(1)
print(f'USD = {rate_usd} ₽')