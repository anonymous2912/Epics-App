from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.factory import Factory

Builder.load_string(
    """
<ExampleBanner@Screen>

    MDBanner:
        id: banner
        over_widget: scroll

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [["dots-vertical", lambda x: None]]
        pos_hint: {"top": 1}

    ScrollView:
        id: scroll
        size_hint_y: None
        height: Window.height - toolbar.height

        MDGridLayout:
            id: box
            adaptive_height: True
            cols: 1
            padding: "10dp"
            spacing: "10dp"

            OneLineListItem:
                text: "What is Depression?"
                on_release:
                    banner.type = "three-line"
                    banner.text = \
                    [\
                    "What is depression?", \
                    "A group of conditions associated with the elevation or lowering of a person's mood, such as depression or bipolar disorder", \
                    "",
                    ]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Causes of Dpression?"
                on_release:
                    banner.type = "two-line"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Levels of Depression?"
                on_release:
                    banner.type = "one-line"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Preventive measures one can take?"
                on_release:
                    banner.type = "three-line-icon"
                    banner.text = \
                    [\
                    "Three line string text example with two actions.", \
                    "This is the second line of the banner message,", \
                    "and this is the third line of the banner message.",
                    ]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Types of Depression"
                on_release:
                    banner.type = "two-line-icon"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Symptoms"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["KNOW MORE", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Cure and Treatment"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = []
                    banner.show()

            OneLineListItem:
                text: "Banner with one actions"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()
"""
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "All About Depression!"
        self.theme_cls.primary_palette = "DeepPurple"

    def build(self):
        self.root = Factory.ExampleBanner()


if __name__ == "__main__":

     MainApp().run()