from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

Builder.load_file('widgets/kv/footer_menu.kv')

class FooterMenu(FloatLayout):
    def switch_screen(self, screen_name):
        App.get_running_app().switch_screen(screen_name)