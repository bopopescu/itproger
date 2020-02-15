from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import ObjectProperty

Window.size = (360, 640)


class Container(BoxLayout):
    get_input = ObjectProperty()
    button_mul = ObjectProperty()
    reset = ObjectProperty()
    buffer = ObjectProperty()
    id7 = ObjectProperty()

    number = 0
    buffer = 0
    zero_have = False
    sign = ""

    # Проверка ввода  - количесво значений введенных в TextInput не может быть больше 10  - 1234567890
    def check_input(self, text):
        if len(self.get_input.text) > 9:
            self.get_input.text = self.get_input.text[:10:]
        else:
            self.get_input.text += text

    def print_operation(self, number, operator):
        self.sign = operator
        self.number = number
        self.clear_display()

    def clear_display(self):
        self.get_input.text = ''

    def do_operation(self, number2):
        if number2 == "" or number2 == "Error":
            self.get_input.text = "0"
            self.clear_display()
        else:
            # print("я buffer do = ", self.buffer)
            if self.sign == "+":
                self.buffer = round((float(self.number) + float(number2)), 10)
                self.get_input.text = str(self.buffer)

            elif self.sign == "-":
                self.buffer = round((float(self.number) - float(number2)), 10)
                self.get_input.text = str(self.buffer)

            elif self.sign == "*":
                self.buffer = round((float(self.number) * float(number2)), 8)
                self.get_input.text = str(self.buffer)

            elif self.sign == "/":
                try:
                    self.buffer = round((float(self.number) / float(number2)), 8)
                    self.get_input.text = str(self.buffer)
                except ZeroDivisionError:
                    self.get_input.text = "Error"
        # print("buffer after = ", self.buffer)

    # Ввод точки для чисел
    def decimal_sign(self):
        if len(self.get_input.text) != 0 and '.' not in self.get_input.text:
            self.get_input.text += "."
        else:
            self.get_input.text = self.get_input.text

    # Добавлена возможность ввести ноль после  - "." например число 0.001234
    def enter_zero(self, text):
        self.get_input.text = '0'
        if self.get_input.text[0] == '0':
            print("ноьл туту")
            print(self.get_input.text)
        elif self.get_input.text[0] and self.get_input.text[1] == ".":
            print("работал этот участо",self.get_input.text)

class CalculatorApp(MDApp):
    title = "Calculator"

    def __init__(self, **kwargs):  # Вызываем self конструктор, а затем ...
        self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)  # вызываем конструктор из базоваого MDApp

    def build(self):
        return Container()


if __name__ == "__main__":
    CalculatorApp().run()
