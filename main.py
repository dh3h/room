import requests

url = 'http://185.209.223.75:3010/game/classic'
response = requests.get(url)

if response.status_code == 200:
    # extract the content from the website
    content = response.text
    # do something with the content
    print(content)
else:
    print('Error accessing website')
