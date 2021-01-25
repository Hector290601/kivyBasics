import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Contenedor01(BoxLayout):
    None

class MainApp(App):
    title = 'Hello World'
    def build(self):
        return Contenedor01()

if __name__ == '__main__':
    MainApp().run()


