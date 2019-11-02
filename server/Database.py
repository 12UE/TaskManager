import pymysql

class Database:
    def __init__(self):
        self.connector = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            db = 'virus',
            password = '',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cursor = self.connector.cursor(cursor=pymysql.cursors.DictCursor)
    def getVirusMd5(self):
        sql = "select * from virus_md5;"
        self.cursor.execute(sql)

        listVirusMd5 = self.cursor.fetchall();
        if(len(listVirusMd5)):
            return listVirusMd5
