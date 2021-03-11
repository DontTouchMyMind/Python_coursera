from bs4 import BeautifulSoup


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
print(soup)
print(soup.prettify())  # Formatted output

print(soup.p)   # <p>
print(type(soup.p))

print(soup.p.b)     # <p><b></b></p>
print(type(soup.p.b))

print(soup.p.b.string)     # <p><b>STRING</b></p>
print(type(soup.p.b.string))

print(soup.b)
print(soup.b.name)

print(soup.p['class'])  # result - list
print(soup.body['id'])  # result - str

print(soup.b.parent)
print(soup.b.parents)

print([tag.name for tag in soup.b.parents])

print(soup.p.next)
print(soup.p.next.next)

print(soup.p.next_sibling.next_sibling)

print(soup.p.contents)  # List
print(soup.p.children)  # Generator
