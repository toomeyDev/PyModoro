from kivy.app import App
from kivy.core.window import Window

# import GUI components
from kivy.uix.label import Label
from kivy.uix.button import Button

# import layout for application
from kivy.uix.boxlayout import BoxLayout

class PyModoro(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        layout = BoxLayout(padding=10)
        lbl_title = Label(text='Pymodoro',
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .5, 'center_y': .90},
                    color=(255,255,255,50))
        layout.add_widget(lbl_title)
        return layout
 

def main():
    
    PyModoro().run()

if __name__ == "__main__":
    main()
