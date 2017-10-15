import sqlite3
import json, requests
api_key = "AIzaSyApuvnawK-aqRhvTW9tsLoKJGT-24fPrvY"
address = "six"
example = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="+api_key
conn =  sqlite3.connect('main.db')
cur = conn.cursor()
cur.execute(""" select * from locations L
                where L.Address not in
                (select L2.Address from locations L2
                where L2.Address = '')""")
res = cur.fetchall()
for i in range(3):
    print(res[i])



url = 'https://maps.googleapis.com/maps/api/geocode/json'

params = dict(
    address="1600 Amphitheatre Parkway, Mountain+View, CA",
    key=api_key,
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(data)