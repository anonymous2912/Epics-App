from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList





Window.size = (300, 500)


class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
       # screen = Builder.load_string(KV)
        return Builder.load_string(KV)

    def on_start(self):
        pass


DemoApp().run()