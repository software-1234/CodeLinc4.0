import sqlite3

from flask import g, jsonify

def get_valid_locations(): 
    conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from locations L
                    where L.Address not in
                    (select L2.Address from locations L2
                    where L2.latitude = '' or L2.latitude is null)""")
    res = cur.fetchall()
    print(res)
    return jsonify(res)

    
def get_valid_locations_non_json(): 
    conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from locations L
                    where L.Address not in
                    (select L2.Address from locations L2
                    where L2.latitude = '' or L2.latitude is null)""")
    res = cur.fetchall()
    print(res)
    return res
    
def get_valid_locations_by_type(typeOfResource):
    conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from locations L
                    where L.TypeofResource = '"""+typeOfResource+"""' and L.Address not in
                    (select L2.Address from locations L2
                    where L2.latitude = '' or L2.latitude is null)""")
    res = cur.fetchall()
    print(res)
    return res
    
def get_home_address_by_phone(number):
    conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from Users u
                    where u.phone_number = """+str(number))
    res = cur.fetchone()
    print(res)
    return (res[9],res[10])
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
