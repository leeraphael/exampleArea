'''
Created on 2014-11-12

@author: raphael
'''
#
# ======================= Ref ======================= 
# sqlite3, https://docs.python.org/2/library/sqlite3.html
#

import sqlite3

def makeConn(dbName = 'exampleDatabase.db'):
    return sqlite3.connect(dbName)

def closeConn(conn):
    conn.close()


def createDB(dbName): 
    makeConn(dbName)
    
def sqlCommand(command): 
    conn = makeConn()
    c = conn.cursor()
    c.execute(command)
    print c.fetchone()
    conn.commit()
    closeConn(conn)    
        
if __name__ == '__main__':
    createDB("testDB.db")
    sqlCommand('''DROP TABLE stocks''')
    sqlCommand('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
    sqlCommand("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    
    symbol = 'RHAT'
    sqlCommand("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

    
    
    