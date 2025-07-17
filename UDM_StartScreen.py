from kivy.uix.screenmanager import Screen
# from kivy.clock import Clock
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.label import MDLabel

from UDM_GSM import GlobalScreenManager, GSM


class StartScreen(Screen):

    def on_enter(self):
        print("Start Screen")
