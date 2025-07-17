from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class GlobalScreenManager(ScreenManager):
    data = 7
    SCREEN_HIST = []

def GSM():
    return MDApp.get_running_app().root