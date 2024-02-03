
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

