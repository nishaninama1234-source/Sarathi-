from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class SarathiApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return Label(text='SARATHI SYSTEM ACTIVE', font_size='30sp', color=(1,1,1,1))

if __name__ == '__main__':
    SarathiApp().run()