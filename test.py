import requests
r = requests.get('https://api.github.com/events')
data = r.text
print(data)


