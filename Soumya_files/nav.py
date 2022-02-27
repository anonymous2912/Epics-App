from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons

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
                     



                    ScreenManager:
                        id: manager

                        MDScreen:
                            name: "one"

                            MDRaisedButton:
                                pos_hint: {"center_x": .5, "center_y": .55}
                                on_release: manager.current = "two"
                                text: "Open Grid"

                        MDScreen:
                            name: "two"

                            ScrollView:
                                do_scroll_x: False

                                MDGridLayout:
                                    cols: 3
                                    row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                    row_force_default: True
                                    adaptive_height: True
                                    padding: dp(6), dp(6)
                                    spacing: dp(6)

                                    SmartTileWithLabel:
                                        text: "What is\\n[size=24]Depression?"
                                        source: "img1.jpg"
                                    SmartTileWithLabel:
                                        text: "Path to\\n[size=24]Happy Life"
                                        source: "img3.jpg"
                                    SmartTileWithLabel:
                                        text: "Daily \\n[size=24]Reports"
                                        source: "img2.jpg"
                                    SmartTileWithLabel:
                                        text: "Fun\\n[size=24]Challenges"
                                        source: "img9.jpeg"
                                    SmartTileWithLabel:
                                        text: "Talk to\\n[size=24]US"
                                        source: "img4.jpg"
                                    SmartTileWithLabel:
                                        text: "Enjoy the\\n[size=24]Relaxing Music"
                                        source: "img5.jpg"
                                    SmartTileWithLabel:
                                        text: "Therapy\\n[size=24]Doctor's Assist"
                                        source: "img7.jpg"
                                    SmartTileWithLabel:
                                        text: "Collect your\\n[size=24]Rewards"
                                        source: "img9.jpg"

                 


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

 
    '''
    

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

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


class TestNavigationDrawer(MDApp):
   # icons = list(md_icons.keys())[15:30]

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
                ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
        
   #     for tab_name in self.icons:
    #        self.root.ids.tabs.add_widget(Tab(icon=tab_name))

            
  #  def on_tab_switch(
       # self, instance_tabs, instance_tab, instance_tab_label, tab_text
    #    ):

       
        #        count_icon = instance_tab.icon
       
          #      print(f"Welcome to {count_icon}' tab'")


TestNavigationDrawer().run()