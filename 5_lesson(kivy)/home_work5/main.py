from PIL.Image import eval
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty

Window.size = (360, 640)


class Container(BoxLayout):
    get_input = ObjectProperty()
    button_mul = ObjectProperty()
    reset = ObjectProperty()
    buffer = ObjectProperty()
    clear_bool = BooleanProperty()

    number = 0
    sign = ""
    buffer = 0

    def print_operation(self, number, operator):
        self.sign = operator
        self.number = number
        self.clear_display()

    def clear_display(self):
        self.get_input.text = ''
        self.clear_bool = False

    def do_operation(self, number2):
        print("я buffer do = ", self.buffer)

        if self.sign == "+":
            print(self.sign)
            self.buffer = float(self.number) + float(number2)
            self.get_input.text = str(self.buffer)

        elif self.sign == "-":
            print(self.sign)
            self.buffer = float(self.number) - float(number2)
            self.get_input.text = str(self.buffer)

        elif self.sign == "*":
            print(self.sign)
            self.buffer = float(self.number) * float(number2)
            self.get_input.text = str(self.buffer)
        elif self.sign == "/":
            try:
                print(self.sign)
                self.buffer = float(self.number) / float(number2)
                self.get_input.text = str(self.buffer)
            except ZeroDivisionError:
                self.get_input.text = "Error"

        print("я buffer posle = ", self.buffer)

    def decimal_sign(self):
        if self.get_input.text[0] != 0 and '.' not in self.get_input.text:
            self.get_input.text += "."


class CalculatorApp(MDApp):
    title = "Calculator"

    def __init__(self, **kwargs):  # Вызываем self конструктор, а затем ...
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)  # вызываем конструктор из базоваого MDApp

    def build(self):
        return Container()


if __name__ == "__main__":
    CalculatorApp().run()

# 1.  Выполнить ввод большего числа
# 2.  Ввод числа с запятой( если нет числа в начале не принимать ввод)
#     и что бы точка была только одна
# 3.  Выполнить сложение двух чисел
#
#
#
#
#
