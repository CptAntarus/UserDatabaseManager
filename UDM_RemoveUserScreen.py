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


    def removeSelections(self):
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

    # User_Table
    # Kiosk_Table
    #[U-Num]
        try:
            cursor.execute("DELETE FROM Kiosk_Table WHERE u_num = ?", 
                           (self.ids.targetUser.text.strip(),))
            conn.commit()
            print("Row deleted successfully.")
        except Exception as e:
            print("Error deleting row:", e)
            conn.rollback()
        finally:
            cursor.execute('SELECT * FROM Kiosk_Table')
            rows = cursor.fetchall()

            # Print each row of the database
            print("REMOTE_DB =====================================")
            for row in rows:
                print(row)
    
    # Rework_Table
        try:
            cursor.execute("DELETE FROM Rework_Table WHERE [U-Num] = ?", 
                           (self.ids.targetUser.text.strip(),))
            conn.commit()
            print("Row deleted successfully.")
        except Exception as e:
            print("Error deleting row:", e)
            conn.rollback()
        finally:
            cursor.execute('SELECT * FROM Rework_Table')
            rows = cursor.fetchall()

            # Print each row of the database
            print("REMOTE_DB =====================================")
            for row in rows:
                print(row)

            conn.close()

            # Switch Back to Start Screen
            MDApp.get_running_app().switchScreen('startScreen')



 