# -*- coding:utf-8 -*-
import random

import pymysql,string,traceback;


class MySQL():
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "database": "life"
    }
    db = None

    def __init__(self):
        self.db = pymysql.connect(**self.config)

    def addRow(self):
        try:
            user = ''.join(random.sample(string.ascii_letters + string.digits, 8)).upper();
            name = "USER" + user;
            sql = "INSERT INTO life_user(name,username,password) VALUES('"+user+"','"+name+"','123456')"
            self.getDB().execute(sql);
        except:
            print("Error: unable to insert data")
    def getRows(self):
        try:
            sql = "SELECT * FROM life_user";
            nowCursor = self.getDB();
            nowCursor.execute(sql);
            data = nowCursor.fetchall();
            print(data);
            # for v in data:
            #     for v2 in v:
            #         print(v2)
        except:
             traceback.print_exc();
    def getDB(self):
        return self.db.cursor()

    # def __del__(self):
    #     self.db.close()

if __name__ == '__main__':
    dbobj = MySQL();
    #dbobj.addRow();
    dbobj.getRows();

