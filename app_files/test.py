from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout 

Builder.load_file('test.kv')

class MyLayout(Widget):
    def checkbox_click(self,instance,value):
        print(instance)

class MainApp(App):
    def build(self):
        self.theme_cls.primary_hue = "200"
        return MyLayout()


if __name__=='__main__':
    MainApp().run()