#!bin/bash

if [ -n "$1" ]; then
	mkdir $1
	touch $1/main.py
	touch $1/main.kv
	echo "import kivy
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

">$1/main.py
else
	echo "Missing parameters, execute by : bash makeBlank.bash targetName"
fi
