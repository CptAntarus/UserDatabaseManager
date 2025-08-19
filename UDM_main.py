#import pyodbc

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

from kivy.lang import Builder
Builder.load_file("UDM_Format.kv")

from UDM_GSM import GlobalScreenManager, GSM
from UDM_StartScreen import StartScreen
from UDM_AddUserScreen import AddUserScreen
from UDM_RemoveUserScreen import RemoveUserScreen
from UDM_LockScreen import LockScreen
from UDM_TimeOut import TimeOut


class UDMGui(MDApp):
    def build(self):
        self.sm = GlobalScreenManager()
        self.sm.add_widget(StartScreen(name='startScreen'))
        self.sm.add_widget(AddUserScreen(name='addUserScreen'))
        self.sm.add_widget(RemoveUserScreen(name='removeUserScreen'))
        self.sm.add_widget(LockScreen(name="lockScreen"))
        self.sm.add_widget(TimeOut(name="timeOut"))

        self.sm.transition = NoTransition()
        self.theme_cls.theme_style = 'Dark'

        return self.sm
    
    def on_start(self):
        GSM().switchScreen('lockScreen')

    

if __name__ == "__main__":
    UDMGui().run()
