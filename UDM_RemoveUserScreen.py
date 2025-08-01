from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from dotenv import load_dotenv
import os
import pyodbc

from UDM_GSM import GlobalScreenManager, GSM


class RemoveUserScreen(Screen):
    def on_enter(self):
        self.ids.targetUser.text = ""
        self.ids.removeUserTopBar.title = GlobalScreenManager.TABLE


    def removeSelections(self):
        load_dotenv("UDM_Creds.env")

        table = GlobalScreenManager.TABLE
        col = GlobalScreenManager.COL

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

        try:
            cursor.execute(f"DELETE FROM {table} WHERE {col} = ?", 
                           (self.ids.targetUser.text.strip(),))
            conn.commit()
            print("Row deleted successfully.")
        except Exception as e:
            print("Error deleting row:", e)
            conn.rollback()
        finally:
            cursor.execute(f'SELECT * FROM {table}')
            rows = cursor.fetchall()

            # Print each row of the database
            print(f"{table} =====================================")
            for row in rows:
                print(row)
    
            # Switch Back to Start Screen
            GSM().switchScreen('startScreen')
