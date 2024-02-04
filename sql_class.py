
import sqlite3
import sys,os
from tkinter import messagebox


class temperature_db():
    
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "test_user"
        self.password = "123456789"
        self.port = 3306
        self.database = "password_db"
        
    
    def conn_db (self):
        database_file = 'temperature.db'
        if os.path.exists(database_file):
            self.my_connector = sqlite3.connect(database_file)
            # 连接数据库后的操作
        else:
            messagebox.showerror(title="数据库链接失败", message="数据库不存在，请将数据库放置到和程序同一目录下！")
            sys.exit()
        self.my_cursor = self.my_connector.cursor()
    
    #数据库关闭
    def conn_close(self):
        self.my_cursor.close()
        self.my_connector.close()

    def on_button_clicked(self,button_name):
        self.conn_db()
        query = "select client_temperature from client_name where client_btn = ?"
        self.my_cursor.execute(query,[button_name])
        result = self.my_cursor.fetchall()
       
        #查询该用户是否存在，如果不存在，插入记录
        if len(result) > 0 :
            self.my_cursor.close()
            return result[0][0]
        else:
            self.my_cursor.close()
            return 0
        