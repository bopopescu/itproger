import pytest
import unittest
import form
import requests


class TestForm(object):
    # Вне функций создайте объект на основе класа форм.
    # В обьект при создании передайте два параметра: login , password
    form_obj = form.Form("admin", "admin_pass")

    # Функция, что протестирует, объект передав в него 2 параметра
    @pytest.mark.fast
    def test_init2(self):
        assert self.form_obj.login == "admin"
        assert self.form_obj.password == "admin_pass"

        form0 = form.Form()
        assert form0.login == "bot"
        assert form0.password == "qwerty"

        form1 = form.Form("admin", "qwerty")
        assert form1.login == "admin"
        assert form1.password == "qwerty"

        form2 = form.Form('user', "1111")
        assert form2.login == "user"
        assert form2.password == "1111"

        form3 = form.Form("vasia", "lolpass", 21)  # "21"
        assert form3.login == "vasia"
        assert form3.password == "lolpass"
        assert type(form3.age) is int
        assert form3.age == 21

    # Функция, что протестирует, объект передав в него 4 параметра
    @pytest.mark.parametrize("test_login, test_password, test_age, test_gender", [
        ("alex234", "my_pass", 32, "m"),
        ("boba", "123", 25, "m"),
        ("Anna", "annapass12345", 30, "fm"),
        # ("bot", "bothackpass", "32", "other")
    ])
    @pytest.mark.fast
    def test_init4(self, test_login, test_password, test_age, test_gender):
        form4 = form.Form(test_login, test_password, test_age, test_gender)
        assert form4.login == test_login
        assert form4.password == test_password
        assert type(form4.age) is int
        assert form4.age == test_age
        assert form4.gender == "m" or form4.gender == "fm"
        assert form4.gender == test_gender

    # Создайте функцию, что протестирует можно ли установить не коректный URL adress веб сайта
    # в переменную url в классе форм
    @pytest.mark.slow
    def test_url(self):
        self.form_obj.url = "http://yandex.ru"  # "http://google.com"  # "yande.dasdqwewqd"  # "http:yandex.ru"
        resp = requests.get(self.form_obj.url)
        assert str(resp) == "<Response [200]>"
        assert resp.status_code == 200


if __name__ == "__main__":
    unittest.main()

# pytest test_form.py -v
