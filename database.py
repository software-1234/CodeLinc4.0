import sqlite3

from flask import g, jsonify

def get_valid_locations(): 
    conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from locations L
                    where L.Address not in
                    (select L2.Address from locations L2
                    where L2.Address = '')""")
    res = cur.fetchall()
    return jsonify(res)

'''
def get_db():
    DATABASE = 'main.db'
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    print("Opened database successfully")
    cur.execute(""" select * from locations L""").fetchall()
    res = cur.fetchall()
    return res
'''
