import requests
import json
def login ():
    my_user = str(input("enter your username: "))
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/user/.json"
    req = requests.get(link)
    dic_req = req.json()

    for id_user in dic_req:
        if my_user == dic_req[id_user]['info']['name']:
            print (f"""name {dic_req[id_user]['info']['name']}
                       telephone {dic_req[id_user]['info']['telephone']}
                       email {dic_req[id_user]['info']['email']}
""")