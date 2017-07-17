import requests , re

reponse = requests.get('https://vimeo.com/channels/staffpicks/videos')

print reponse.text