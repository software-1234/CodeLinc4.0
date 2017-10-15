import sqlite3
import json, requests
api_key = "AIzaSyApuvnawK-aqRhvTW9tsLoKJGT-24fPrvY"
address = "six"
example = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="+api_key
with sqlite3.connect('main.db') as conn:
    #conn =  sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute(""" select * from Users L
                    where L.Address not in
                    (select L2.Address from Users L2
                    where L2.Address = '')""")

    res = cur.fetchall()
    print(len(res))
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    for i in range(0,1):
        print(i)
        print(res[i])
        id = res[i][0]
        print(id)
        address_string = res[i][6] + ", "+ res[i][7] + ", "+ res[i][8]
        print(address_string)
        params = dict(
            address= address_string,
            key=api_key,
        )

        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        lat = data["results"][0]["geometry"]["location"]["lat"]
        lng = data["results"][0]["geometry"]["location"]["lng"]
        print(lat, lng)
        cur.execute(""" Update Users
                        Set latitude="""+str(lat)+""", longitude="""+str(lng)+"""
                        Where phone_number="""+str(id))        