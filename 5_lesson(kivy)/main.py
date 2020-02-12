from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class DuckyApp(App):
    def build(self):
        # box = BoxLayout()
        # b1 = Button(text="Hi all!")
        # b2 = Button(text="Hi all2!")
        # box.add_widget(b1)
        # box.add_widget(b2)
        return Container()


if __name__ == "__main__":
    DuckyApp().run()
