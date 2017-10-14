import sqlite3

from flask import g

DATABASE = '/db/main.db'

def print_hi():
    return "hi"
def get_db(): 
    conn =  sqlite3.connect('main.db')
    #db = getattr(g, '_database', None)
    #if db is None:
    #    db = g._database = sqlite3.connect(DATABASE)
    print("Opened database successfully")
    #return conn
    cur = conn.cursor()
    print("created cursor")
    cur.execute(""" select * from locations L""")
    for row in cur:
        print(row)
    return 'hi'

#@app.teardown_appcontext
#def close_connection(exception):
#    db = getattr(g, '_database', None)
#    if db is not None:
#        db.close()
