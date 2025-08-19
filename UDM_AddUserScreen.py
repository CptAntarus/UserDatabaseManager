from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from dotenv import load_dotenv
import os
#import pyodbc
import pymssql

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
        #load_dotenv("UDM_Creds.env")

        table = GlobalScreenManager.TABLE
        col = GlobalScreenManager.COL

        print("TABLE:",GlobalScreenManager.TABLE)
        print("COL:",GlobalScreenManager.COL)
        
        load_dotenv("UDM_Creds.env")
        ######Used by pyodbc#######
        #driver = os.getenv('DRIVER')
        svr = os.getenv('SERVER')
        db = os.getenv('DATABASE')
        uid = os.getenv('USR')
        pwd = os.getenv('PASS')
        
        conn = pymssql.connect(server=svr, user=uid, password=pwd, database=db,)
        cursor = conn.cursor()

        user_id = self.ids.newUNum.text.strip()
        userName = self.ids.newUser.text.strip()
        basicPerm = self.basicUserPerm
        reworkPerm = self.ReworkUserPerm
        bgaPerm = self.BGAUserPerm
        adminPerm = self.AdminUserPerm
        qaPerm = self.QAUserPerm
        pin = self.ids.newPin.text.strip()
        #Error inserting data: (102, b"Incorrect syntax near '?'.DB-Lib error message 20018, severity 15:\nGeneral SQL Server error: Check messages from the SQL Server\n")
        try:
            merge_query = f"""
            MERGE INTO {table} AS target
            USING (SELECT ? AS {col}) AS source
            ON target.{col} = source.{col}
            WHEN MATCHED THEN
                UPDATE SET
                    Name = ?,
                    Basic_Access = ?,
                    Rework = ?,
                    BGA = ?,
                    Admin = ?,
                    QA = ?,
                    PIN = ?
            WHEN NOT MATCHED THEN
                INSERT ({col}, Name, Basic_Access, Rework, BGA, Admin, QA, PIN)
                VALUES (?,?,?,?,?,?,?,?);
            """
            
            merge_params = (
                  user_id,
                  userName, basicPerm, reworkPerm, bgaPerm, adminPerm, qaPerm, pin,

                  user_id, userName, basicPerm, reworkPerm, bgaPerm, adminPerm, qaPerm, pin 
            )

            cursor.execute(merge_query, merge_params)
            conn.commit()
            print("Data inserted successfully.")
            print("Added: ",user_id)

        except Exception as e:
            print("Error inserting data:", e)
            conn.rollback()

        finally:
            cursor.execute(f'SELECT * FROM {table}')
            rows = cursor.fetchall()

            # Print each row of the database
            print(f"{table} =====================================")
            for row in rows:
                print(row)

            conn.close()

            # Switch Back to Start Screen
            GSM().switchScreen('startScreen')
