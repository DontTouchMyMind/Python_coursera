from bs4 import BeautifulSoup
import re


html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test page</title>
</head>
<body class="my_body" id="js-body">
    <p class="text odd">first <b>bold</b> paragraph</p>
    <p class="text even">second <a href="https://mail.ru">link</a></p>
    <p class="list odd">third <a id="paragraph"><b>bold link</b></a>paragraph</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
#
# # Найти родителя тега <b>, у которого id='js-body'
# print(soup.p.b.find_parent(id='js-body').name)
# print(soup.p.b.find_parent('body')['id'])
#
# # Найти следующего соседа тега <p> и отфильтровать по классу
# print(soup.p.find_next_sibling(class_='odd'))
# print(soup.p.find_next_siblings())
#
# print(soup.p.find('b'))
#
# print(soup.find(id='js-body')['class'])
#
# print(soup.find_all('p'))
# print(soup.find_all('p', 'text odd'))

print(soup.select('p.odd.text'))

# Найти 3-ий из тегов <p>
print(soup.select('p:nth-of-type(3)'))

# Найти тэг b внутри а
print(soup.select('a > b'))


# ИСПОЛЬЗОВАНИЕ re
result = [i.name for i in soup.find_all(name=re.compile('^b'))]
print(result)

# Найти все теги a и b
result = [i for i in soup(['a', 'b'])]
print(result)


# Изменение тегов
tag = soup.b
tag.name = 'i'
tag['i'] = 'myid'
tag.string = 'italic'
print(soup.p)
print(soup)