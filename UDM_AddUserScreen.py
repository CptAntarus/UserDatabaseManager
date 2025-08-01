from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from dotenv import load_dotenv
import os
import pyodbc

from UDM_GSM import GlobalScreenManager, GSM


class AddUserScreen(Screen):
    def on_enter(self):
        self.basicUserPerm = 0
        self.ReworkUserPerm = 0
        self.BGAUserPerm = 0
        self.AdminUserPerm = 0
        self.QAUserPerm = 0

        self.ids.basicUserIcon.opacity = 0
        self.ids.ReworkUserIcon.opacity = 0
        self.ids.BGAUserIcon.opacity = 0
        self.ids.AdminUserIcon.opacity = 0
        self.ids.QAUserIcon.opacity = 0

        self.ids.newUNum.text = ""
        self.ids.newUser.text = ""
        self.ids.newPin.text = ""

        self.ids.addUserTopBar.title = GlobalScreenManager.TABLE


    def toggleBasicUserIcon(self):
            self.basicUserPerm = 0 if self.basicUserPerm else 1
            self.ids.basicUserIcon.opacity = 1 if self.basicUserPerm else 0
    def toggleReworkUserIcon(self):
            self.ReworkUserPerm = 0 if self.ReworkUserPerm else 1
            self.ids.ReworkUserIcon.opacity = 1 if self.ReworkUserPerm else 0
    def toggleBGAUserIcon(self):
            self.BGAUserPerm = 0 if self.BGAUserPerm else 1
            self.ids.BGAUserIcon.opacity = 1 if self.BGAUserPerm else 0
    def toggleAdminUserIcon(self):
            self.AdminUserPerm = 0 if self.AdminUserPerm else 1
            self.ids.AdminUserIcon.opacity = 1 if self.AdminUserPerm else 0
    def toggleQAUserIcon(self):
            self.QAUserPerm = 0 if self.QAUserPerm else 1
            self.ids.QAUserIcon.opacity = 1 if self.QAUserPerm else 0

    def submitSelections(self):
        load_dotenv("UDM_Creds.env")

        table = GlobalScreenManager.TABLE
        col = GlobalScreenManager.COL

        print("TABLE:",GlobalScreenManager.TABLE)
        print("COL:",GlobalScreenManager.COL)
 
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
        
        insert_query = f'''
            INSERT INTO {table} ({col}, Name, Basic_Access, Rework, BGA, Admin, QA, pin)
            VALUES (?,?,?,?,?,?,?,?)
        '''
        data = (
                self.ids.newUNum.text.strip(),
                self.ids.newUser.text.strip(),
                self.basicUserPerm,
                self.ReworkUserPerm,
                self.BGAUserPerm,
                self.AdminUserPerm,
                self.QAUserPerm,
                self.ids.newPin.text.strip()
              )

        try:
            cursor.execute(insert_query, data)
            conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Error inserting data:", e)
            conn.rollback()
        finally:
            cursor.execute(f'SELECT * FROM {table}')
            rows = cursor.fetchall()

            print("Added: ",data)
            # Print each row of the database
            print(f"{table} =====================================")
            for row in rows:
                print(row)

            conn.close()

            # Switch Back to Start Screen
            GSM().switchScreen('startScreen')
