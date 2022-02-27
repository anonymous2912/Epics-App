from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.color_definitions import colors


KV= """



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
                        id: toolbar
                        title: "Dealing with Depression"
                        md_bg_color: app.theme_cls.primary_light
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        
                    Widget:

                MDBanner:
                    id: banner
                    over_widget: scroll
                    #pos_hint: {"center_x": 0.5, "center_y": 0.5}



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
                                import webbrowser
                                banner.icon="icons/i2.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "What is Depression?", \
                                "Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest. ",\
                                "Also called major depressive disorder or clinical depression.",
                                
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.psychiatry.org/patients-families/depression/what-is-depression')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()

                        OneLineListItem:
                            
                            text: "Causes of Depression"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i5.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "What causes Depression?", \
                                "Lots of things can increase the chance of depression, including abuse, age, conflict, death,", \
                                "genes, other serious illnesses",
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.webmd.com/depression/guide/causes-depression')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()

                        OneLineListItem:
                            
                            text: "Signs of Depression"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i1.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "What are the various symptoms of depression?", \
                                "Feelings of sadness, tearfulness, emptiness or hopelessness Angry outbursts, irritability ", \
                                "or frustration, even over small matters",
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.healthline.com/health/depression/recognizing-symptoms')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()


                        OneLineListItem:
                            
                            text: "Depression Is Different From Sadness or Grief/Bereavement"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i4.jpeg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "How is depression different from sadness or grief/bereavement?", \
                                "Sadness is an emotion that everyone experiences, often after stressful or upsetting life events. ", \
                                "Whereas depression is an overpowering and ongoing mental health disorder.",
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.healthline.com/health/depression/depression-vs-sadness')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()


                        OneLineListItem:
                            
                            text: "Types of Depression"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i3.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "what are the varoius types of depression?", \
                                "There are many different types of depression. Events in your life cause some, and chemical", \
                                "changes in your brain cause others.",
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.webmd.com/depression/guide/depression-types')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()


                        OneLineListItem:
                            
                            text: "Take Help"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i7.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "Psychotherapy", \
                                "Psychotherapy is a general term for treating depression by talking about your condition and",\
                                "related issues with a mental health professional and get the right assistance and comfort .", 
                                
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.verywellmind.com/types-of-psychotherapy-for-depression-1067407')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()


                        OneLineListItem:
                            
                            text: "About Antidepressants"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i12.png"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "All about Antidepressants", \
                                "Antidepressants are medications used to treat major depressive disorder, some anxiety disorders,",\
                                "some chronic pain conditions, and to help manage some addictions . ", 
                                
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.medicalnewstoday.com/articles/248320')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()


                        OneLineListItem:
                            
                            text: "Read to Cope Up with Depression"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i10.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "Read for Self Improvement", \
                                "Books are a great escape from the stresses of the real world, a fact that may be especially true for",\
                                "those battling depression.Books can be the best companion for such people.", 
                                
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.bestcounselingdegrees.net/resources/depression-self-help-books/')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()

                        OneLineListItem:
                            
                            text: "Importance of Self Care"
                            on_release:
                                import webbrowser
                                banner.icon="icons/i9.jpg"
                                banner.type = "three-line-icon"
                                banner.text = \
                                [\
                                "How important is self care?", \
                                "Engaging in a self-care routine has been clinically proven to reduce or eliminate depression",\
                                "increase happiness, improve energy, and more.", 
                                
                                ]
                                banner.left_action = ["KNOW MORE", lambda x: webbrowser.open('https://www.snhu.edu/about-us/newsroom/health/what-is-self-care')]
                                banner.right_action = ["CLOSE", lambda x: banner.hide()]
                                banner.show()



                        


                        


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

            
"""


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
            if item.text_color == self.theme_cls.primary_light:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_light



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_hue = "200"
        return Builder.load_string(KV)

    


    def on_start(self):
        icons_item = {
            "folder": "My Reports",
            "account-multiple": "Profile",
            "star": "coins",
            "history": "Recent",
             "checkbox-marked": "Challenge Checklist",
            "logout":"Logout",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


if __name__ == "__main__":
    MainApp().run()