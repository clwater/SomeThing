import re
import requests


def getDataFrom(index):
    reponse = requests.get('https://www.pexels.com/?format=js&page='+str(index) )
    # reponse.encoding = 'utf-8'
    html = reponse.text

    print html



    if '\\n\\n\\n' in html:
        return False
    else:

        html = html.replace('\\n', '')
        # print html
        _article = re.findall('data-photo-id.*?>', html)
        for id in _article:
            # print id
            id = id.replace('data-photo-id=\\"', '')
            id = id.replace('\\">', '')
            # print id
            image = 'https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg' % (id, id)
            print image
        return True


def getData():

    index = 0

    _get = True
    while _get :
        index = index + 1
        _get = getDataFrom(index)



getData()
# getDataFrom(10000)



