
def get_cleaned_url(url: str):
    result = None

    if url.find('?') == -1:
        clearedURL = url
    else:
        clearedURL = url[0:url.find('?')]

    clearedURL = clearedURL.replace('www.', '')
    clearedURL = clearedURL.replace('https://', '')

    url_split = list(filter(None, clearedURL.split('/')))
    if url_split[-2] == 'in' or url_split[-2] == 'company':
        result = '/'.join(url_split)
    elif url_split[1] == 'in' or url_split[1] == 'company':
        result = '/'.join(url_split[:3])

    return result

def checkNick(nick):
    if type(nick) == str:
        if nick.find('?') == -1:
            try:
                intName = int(nick)
                if str(intName) != nick:
                    raise Exception('incorrect int / correct nick')
                result = False
            except:
                result = True
        else:
            result = False
    else:
        result = False

    return result

def getNickFromURL(url):
    result = None

    url = get_cleaned_url(url)
    splitedURL = url.split('/')
    if splitedURL[-2] == 'in' or splitedURL[-2] == 'company':
        nameZone = splitedURL[-1]

        if checkNick(nameZone) == True:
            result = nameZone

    return result

def checkID(id):
    if type(id) == str:
        try:
            intID = int(id)
            if str(intID) == id:
                result = True
            else:
                result = False
        except:
            result = False
    elif type(id) == int:
        if id > 0:
            result = True
        else:
            result = True
    else:
        result = False

    return result

def getIdFromURL(url):
    result = None

    url = get_cleaned_url(url)
    splitedURL = url.split('/')
    if splitedURL[-2] == 'in' or splitedURL[-2] == 'company':
        identificator = splitedURL[-1]

        if checkID(identificator) == True:
            result = int(identificator)

    return result