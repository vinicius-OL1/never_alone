import requests
import json
def login (user,password):
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/user/.json"
    req = requests.get(link)
    dic_req = req.json()
    for id_user in dic_req:
        try:
            if user == dic_req[id_user]['info']['name'] and password == dic_req[id_user]['info']['password']:
                print (f"""
                       name: {dic_req[id_user]['info']['name']}
                       telephone: {dic_req[id_user]['info']['telephone']}
                       email: {dic_req[id_user]['info']['email']}
                          \n
                        """)
                break
        
            
        except KeyError:
            print ("user not found")
            break
        
            