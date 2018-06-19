from kivy.app import App
from kivy.uix.label import Label

class TicTacToeApp(App):
    def build(self):
        return Label(text='Fuck You',
        font_size=100,
        color=(0, 1, 0, 1))

if __name__ == "__main__":
    TicTacToeApp().run()