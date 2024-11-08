# pip install requests
import requests

# data = requests.get('https://yle.fi/')
# print(data.text)

käyttäjät = requests.get('https://jsonplaceholder.typicode.com/users')
tehtävät = requests.get('https://jsonplaceholder.typicode.com/todos')

# print(len(käyttäjät.json())) # 10
