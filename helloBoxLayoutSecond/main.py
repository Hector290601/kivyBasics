import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Box01(BoxLayout):
    def __init__(self):
        super(Box01, self).__init__()
        self.BR = BRed()
        self.BG = BGreen()
        self.BB = BBlue()
        self.add_widget(self.BR)
        self.add_widget(self.BG)
        self.add_widget(self.BB)
        #self.add_widget(BoxLayout())
        self.BR.add_widget(BBlue())
        self.BR.add_widget(BBlue())
        self.BG.add_widget(BBlue())
        self.BG.add_widget(BBlue())

class BRed(BoxLayout):
    None

class BBlue(BoxLayout):
    None

class BGreen(BoxLayout):
    None

class MainApp(App):
    title = 'Hello World'
    def build(self):
        return Box01()

if __name__ == '__main__':
    MainApp().run()


