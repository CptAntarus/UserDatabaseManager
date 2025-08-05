import os
import pyodbc
from dotenv import load_dotenv
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu

from UDM_GSM import GlobalScreenManager, GSM


class StartScreen(Screen):
#################################################################################
#        - ADD
#################################################################################
    def openMenuAdd(self,caller):
        options = ["User Database"]

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

#################################################################################
#        - REMOVE
#################################################################################
    def openMenuRemove(self,caller):
        options = ["User Database", "Rework Table", "Kiosk Table", "History Table"]

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
        elif text == 'History Table':
            GlobalScreenManager.TABLE = "History_Table"
            GlobalScreenManager.COL = "[u-num]"
        else:
            print("Error with Assigning TABLE")
        self.menu.dismiss()
            
        GSM().switchScreen('removeUserScreen')

#################################################################################
#        - SHOW
#################################################################################
    def openMenuShow(self, caller):
        options = ["User Database", "Rework Table", "Kiosk Table", "History Table", "Oven Table"]

        menu_items = [ {"text": i,"on_release": lambda x=i: self.selectOptionShow(x)}
            for i in options ]

        self.menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            width_mult=3,
        )
        self.menu.open()

    def selectOptionShow(self, text):
        if text == 'User Database':
            table = "User_Table"
        elif text == 'Rework Table':
            table = "Rework_Table"
        elif text == 'Kiosk Table':
            table = "Kiosk_Table"
        elif text == 'History Table':
            table = "History_Table"
        elif text == 'Oven Table':
            table = "Oven_Log"
        else:
            print("Error with Assigning TABLE")
        self.menu.dismiss()

        load_dotenv("UDM_Creds.env")
        driver = os.getenv('DRIVER')
        server = os.getenv('SERVER')
        database = os.getenv('DATABASE')
        uid = os.getenv('UID')
        pwd = os.getenv('PWD')

        conn = pyodbc.connect(
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={uid};'
            f'PWD={pwd};'
            'TrustServerCertificate=yes;'
        )
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()

        # Print each row of the database
        print(f"{table} =====================================")
        for row in rows:
            print(row)

        conn.close()