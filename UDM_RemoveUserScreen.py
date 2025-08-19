from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from dotenv import load_dotenv
import os
#import pyodbc
import pymssql

from UDM_GSM import GlobalScreenManager, GSM


class RemoveUserScreen(Screen):
    def on_enter(self):
        self.ids.targetUser.text = ""
        self.ids.targetUser.focus = True
        self.ids.removeUserTopBar.title = GlobalScreenManager.TABLE


    def removeSelections(self):

        table = GlobalScreenManager.TABLE
        col = GlobalScreenManager.COL
        
        load_dotenv("UDM_Creds.env")
        ######Used by pyodbc#######
        #driver = os.getenv('DRIVER')
        svr = os.getenv('SERVER')
        db = os.getenv('DATABASE')
        uid = os.getenv('USR')
        pwd = os.getenv('PASS')
       
        conn = pymssql.connect(server=svr, user=uid, password=pwd, database=db,)
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
