import sqlite3
class LogMessageDB:
    
    def __init__(self,dbname):
        self.dbname = dbname
        db = sqlite3.connect(self.dbname)
        db.execute('create table if not exists LogMessage (message)')
        db.commit()
        db.close()
    def read(self):
        db = sqlite3.connect(self.dbname)
        data = db.execute('select * from LogMessage')
        for each in data:
            print(each)
        db.close()
    def write(self,message):
        db = sqlite3.connect(self.dbname)
        db.execute('insert into LogMessage (message) values (?)', (message,))
        db.commit()
        db.close()
        
class LogMessageFile:
    def __init__(self,filename):
        self.filename = filename
    def read(self):
        f = open(self.filename,'r')
        lines = f.readlines()
        for each in lines:
            print(each, end='')
    def write(self,message):
        f = open(self.filename, 'a')
        f.write(message)
    