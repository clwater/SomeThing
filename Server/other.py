import requests

# reponse = requests.get('http://vimeo.com')
reponse = requests.get('https://www.google.com/')
# reponse = requests.get('http://vimeo.com/channels/staffpicks/videos/page:1')
html = reponse.text

print html