import requests


reponse = requests.get('https://www.pexels.com/')



html = reponse.text

print html