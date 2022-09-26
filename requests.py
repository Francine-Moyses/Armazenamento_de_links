import requests

response = requests.get('http://127.0.0.1:5000/links')

if response.status_code == 200:
    message = response.json()
    print(message['lista'])
else:
    print(response.status_code)
