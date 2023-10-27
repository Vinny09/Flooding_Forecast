from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("tela1.kv")

class Tela1(Screen):
    pass

class Tela2(Screen):
    pass

class Screens(ScreenManager):
    pass

class myapp(App):
    def build(self):
        return Screens()
if __name__ == '__main__':
    myapp().run()
