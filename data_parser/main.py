import requests
from bs4 import BeautifulSoup as bs4

# заголовки
# если не отправлять заголовки, браузер подумает что мы робот

headers = {
    'accept': '*/*',
    'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
}

url = "https://itproger.com/"
session = requests.Session()

try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        print("Ok")
        soup = bs4(req.content, "html.parser")
        divs = soup.find_all('div', attrs={'class': 'article'})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print(title, " -  https://itproger.com/{}".format(href))
    else:
        print("Error")
except Exception:
    print("ошибка в самом URL адресе")
