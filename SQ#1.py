import sqlite3
connection = sqlite3.connect("CASE.db")
cursor = connection.cursor()
def TEXT():
    cursor.execute("SELECT autherName FROM auther")
    data = cursor.fetchall()#only needed during extraction of info
#TEXT()
def CON():
    cursor.execute("CREATE TABLE IF NOT EXISTS CA(CAT_NAME TEXT,APPLE_NAME TEXT)")
CON()
connection.commit()#save changes
cursor.close()#close curser before connection//required
connection.close()
