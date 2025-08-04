from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class GlobalScreenManager(ScreenManager):
    data = 7
    TABLE = ""
    COL = ""
    SCREEN_HIST = []

    def switchScreen(self, newScreen):
        GlobalScreenManager.SCREEN_HIST.append(self.current)
        self.current = newScreen

    def backButton(self, *args):
        self.current = GlobalScreenManager.SCREEN_HIST.pop()

    def lockOut(self):
        self.reset()
        self.switchScreen("lockScreen")

    def reset(self):
        GlobalScreenManager.SCREEN_HIST.clear()
        GlobalScreenManager.TABLE = ""


def GSM():
    return MDApp.get_running_app().root