class Form(object):
    url = ""

    def __init__(self, login="bot", password="qwerty", age=18, gender="m"):
        self.login = login
        self.password = password
        self.age = age  # + 2 (make some errors)
        self.gender = gender  # + 2
