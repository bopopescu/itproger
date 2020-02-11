import requests
import urllib3


class Form(object):
    url = ""

    def __init__(self, login="bot", password="qwerty", age=18, gender="m"):
        self.login = login
        self.password = password
        self.age = age  # + 2 (make some errors)
        self.gender = gender  # + 2

#    def check_url(self):
#        try:
#            response = requests.get(self.url)
#            print(response)
#            if response.status_code == 200:
#                print("Working url")
#            else:
#                print("Not working url")
#        except urllib3.exceptions.NewConnectionError as ex:
#            print(ex)
#        except urllib3.exceptions.MaxRetryError as exe:
#            print(exe)
#        except requests.exceptions.ConnectionError as excep:
#            print(excep)


# form1 = Form()
# form1.url = "http://ya"
# form1.check_url()
