from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set("graphics", "resizeable", "0")
#Config.set("graphics", "width", "480") WTF
#Config.set("graphics", "height", "853") WTF
Window.size = (480, 853)

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
            self.ids.result.text = "Неккоректное число!"
    def convertOct(self):
        try:
            num = int(self.ids.number.text)
            self.ids.result.text = oct(num)
        except:
            self.ids.result.text = "Неккоректное число!"
    def convertHex(self):
        try:
            num = int(self.ids.number.text)
            self.ids.result.text = hex(num)
        except:
            self.ids.result.text = "Неккоректное число!"

    def convertRome(self):
        data = int(self.ids.number.text)
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[data // 1000]
        h = hunds[data // 100 % 10]
        te = tens[data // 10 % 10]
        o = ones[data % 10]
        self.ids.result.text = t + h + te + o

    def convertMorse(self):
        data = str(self.ids.number.text)
        morse = {'а': '.-',
                        '0': '-----',
                        '1': '.----',
                        '2': '..---',
                        '3': '...--',
                        '4': '....-',
                        '5': '.....',
                        '6': '-....',
                        '7': '--...',
                        '8': '---..',
                        '9': '----.',
                        }
        result = []
        for element in data:
            result.append(morse[element])
        self.ids.result.text = ''.join(result)

class ConvertApp(MDApp):
    def build(self):
        self.title = 'Python Convert'
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='menu'))

        return self.sm

if __name__ == "__main__":
    ConvertApp().run()