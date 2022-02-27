from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "images.png"

    MDLabel:
        text: "User Name"
        font_style: "Button"
        adaptive_height: True

    MDLabel:
        text: "user@gmail.com"
        font_style: "Caption"
        adaptive_height: True

    ScrollView:

        DrawerList:
            id: md_list



MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Depression Breakthrough"
                        md_bg_color: app.theme_cls.accent_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:

                MDCard:
                    orientation: "vertical"
                    padding: "2dp"
                    size_hint: None, None
                    size: "680dp", "400dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    Image:
                        id: avatar
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        size_hint: None, None
                        size: "450dp", "550dp"
                        source: "img4.jpg"

                        
                   

                    MDLabel:
                        text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et aliquet tortor. Curabitur vitae eros elit. Nam nec feugiat risus, ut venenatis purus. Praesent tristique lectus ut ligula gravida maximus. Cras ac turpis lacinia quam lacinia feugiat. Praesent metus odio, rhoncus ac dolor vel, varius dignissim magna. Mauris pulvinar justo ex, sed aliquam risus facilisis vel. Vestibulum consectetur finibus sem non eleifend. Nam dictum consectetur dolor eget convallis."


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class DepressionBreakthrough(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "folder": "My Reports",
            "account-multiple": "Profile",
            "star": "coins",
            "history": "Recent",
             "checkbox-marked": "Challenge Checklist",
            # "upload": "Upload",
            "logout":"Logout",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


DepressionBreakthrough().run()