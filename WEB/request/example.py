import requests
import json


# Simple request
r = requests.get('http://httpbin.org/get')
print(f'Simple GET request:\n {r} \n {r.text}\n')

r = requests.post('http://httpbin.org/post')
print(f'Simple POST request:\n {r.text}\n')


# Passing Parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(f'GET with passing parameters:\n{r.text}\n')

r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(f'PUT with passing parameters:\n{r.text}\n')


# JSON
url = 'http://httpbin.org/post'
r = requests.post(url, json={'key': 'value'})
print(f'POST with JSON-data:\n{r.text}\n')


# POST a Multipart-Encoding File
url = 'http://httpbin.org/post'
files = {
    'file': (
        'test.txt',
        open('/media/WorkSpace/Project/Python/Python_coursera/WEB/request/test.txt', 'rb')
    )
}
r = requests.post(url, files=files)
print(f'POST with file:\n{r.text}\n')


# HEADERS
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my_app/0.0.1'}
r = requests.get(url, headers=headers)
print(f'GET with headers:\n{r.text}\n')


# Response Content
url = 'http://httpbin.org/get'
r = requests.get(url)
print(type(r.text), r.text)
print(type(r.content), r.content)
print(type(r.json()), r.json())

# Response Status Code
print(r.status_code)
print(r.status_code == requests.codes.ok)

# Response Headers
print(r.headers)

# Bad request
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()


# Redirection and history
url = 'http://github.com'
r = requests.get(url)
print(f'URL:{r.url}')
print(f'CODE:{r.status_code}')
print(f'HISTORY:{r.history}')

r = requests.get(url, allow_redirects=False)
print(f'CODE:{r.status_code}')
print(f'HISTORY:{r.history}')


# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(f'COOKIES: {r.text}')

# Session Objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sesioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(f'COOKIE: {s.cookies}')
print(f'Response: {r.text}')

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)