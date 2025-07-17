import pyodbc

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

from kivy.lang import Builder
Builder.load_file("UDM_Format.kv")

from UDM_GSM import GlobalScreenManager, GSM
from UDM_StartScreen import StartScreen
from UDM_AddUserScreen import AddUserScreen
from UDM_RemoveUserScreen import RemoveUserScreen


class UDMGui(MDApp):
    def build(self):
        self.sm = GlobalScreenManager()
        self.sm.add_widget(StartScreen(name='startScreen'))
        self.sm.add_widget(AddUserScreen(name='addUserScreen'))
        self.sm.add_widget(RemoveUserScreen(name='removeUserScreen'))

        self.sm.transition = NoTransition()
        self.theme_cls.theme_style = 'Dark'

        return self.sm
    
    def on_start(self):
        self.switchScreen('startScreen')

    def switchScreen(self, newScreen):
        GlobalScreenManager.SCREEN_HIST.append(self.sm.current)
        self.sm.current = newScreen

    def backButton(self, *args):
        self.sm.current = GlobalScreenManager.SCREEN_HIST.pop()

    def reset(self):
        GlobalScreenManager.SCREEN_HIST.clear()

if __name__ == "__main__":
    UDMGui().run()

# def read_from_remote_db():
#     # Connect to the remote MySQL database
#     conn = pyodbc.connect(
#         driver='ODBC Driver 17 for SQL Server',
#         host='USW-SQL30003.rootforest.com',
#         user='OvenBakedUsr',
#         password='aztmvcjfrizkcpdcehky',
#         database='Oven_Bake_Log'
#     )
#     cursor = conn.cursor()
 

#     ##############################################

#     try:
#         cursor.execute("DELETE FROM User_Table WHERE [U-Num] = ?", ('U312110',))
#         conn.commit()
#         print("Row deleted successfully.")
#     except Exception as e:
#         print("Error deleting row:", e)
#         conn.rollback()
#     finally:
#         pass
#         # conn.close()

#     ##############################################

#     # insert_query = '''
#     # INSERT INTO User_Table ([U-Num], Name, Basic_Access, Rework, BGA, Admin)
#     # VALUES (?,?,?,?,?,?)
#     # '''
#     # data = ('U', 'Benjamin Barger', '1','1','1','1')

#     # try:
#     #     cursor.execute(insert_query, data)
#     #     conn.commit()
#     #     print("Data inserted successfully.")
#     # except Exception as e:
#     #     print("Error inserting data:", e)
#     #     conn.rollback()
#     # finally:
#     #     conn.close()

#     ###############################################

#     cursor.execute('SELECT * FROM User_Table')
#     rows = cursor.fetchall()

#     # Print each row
#     print("REMOTE_DB =====================================")
#     for row in rows:
#         print(row)

#     # # Close the connection
#     conn.close()


# print("Start...")

# read_from_remote_db()

# print("Done!")