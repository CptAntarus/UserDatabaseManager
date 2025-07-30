from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu

from UDM_GSM import GlobalScreenManager, GSM


class StartScreen(Screen):

    def on_enter(self):
        print("Start Screen")

    def openMenuAdd(self,caller):
        options = ["User Database", "Rework Table", "Kiosk Table"]

        menu_items = [ {"text": i,"on_release": lambda x=i: self.selectOptionAdd(x)}
            for i in options ]

        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            width_mult=3,
        )
        self.menu.open()

    def selectOptionAdd(self, text):
        if text == 'User Database':
            GlobalScreenManager.TABLE = "User_Table"
            GlobalScreenManager.COL = "[U-Num]"
        elif text == 'Rework Table':
            GlobalScreenManager.TABLE = "Rework_Table"
            GlobalScreenManager.COL = "[u-num]"
        elif text == 'Kiosk Table':
            GlobalScreenManager.TABLE = "Kiosk_Table"
            GlobalScreenManager.COL = "u_num"
        else:
            print("Error with Assigning TABLE")
        self.menu.dismiss()
            
        GSM().switchScreen('addUserScreen')

    def openMenuRemove(self,caller):
        options = ["User Database", "Rework Table", "Kiosk Table"]

        menu_items = [ {"text": i,"on_release": lambda x=i: self.selectOptionRemove(x)}
            for i in options ]

        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            width_mult=3,
        )
        self.menu.open()

    def selectOptionRemove(self, text):
        if text == 'User Database':
            GlobalScreenManager.TABLE = "User_Table"
            GlobalScreenManager.COL = "[U-Num]"
        elif text == 'Rework Table':
            GlobalScreenManager.TABLE = "Rework_Table"
            GlobalScreenManager.COL = "[u-num]"
        elif text == 'Kiosk Table':
            GlobalScreenManager.TABLE = "Kiosk_Table"
            GlobalScreenManager.COL = "u_num"
        else:
            print("Error with Assigning TABLE")
        self.menu.dismiss()
            
        GSM().switchScreen('removeUserScreen')