from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set("graphics", "resizeable", "0")
#Config.set("graphics", "width", "480") WTF
#Config.set("graphics", "height", "853") WTF
#Window.size = (480, 853)

class service_get_set():
    def __init__(self, number=""):
        self.number = number
    def get_number(self):
        return self.number
    def set_number(self, x):
        self.number = x
service = service_get_set()
class MainScreen(Screen): #Основное окно
    def convertBin(self):
        try:
            num = int(self.ids.number.text)
            self.ids.result.text = bin(num)
        except:
            pass
    def convertHex(self):
        try:
            num = int(self.ids.number.text)
            self.ids.result.text = hex(num)
        except:
            pass

class ConvertApp(MDApp):
    def build(self):
        self.title = 'Python Chat'
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='menu'))

        return self.sm

if __name__ == "__main__":
    ConvertApp().run()