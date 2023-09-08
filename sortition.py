import requests
import json
import random
def sortition():
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/user/.json"
    req = requests.get(link)
    dic_req = req.json()
    users = []
    for id_user in dic_req:
        users.append(id_user)
    random_user = random.choice(users)
    print (random_user)
    for id_user in dic_req:
        if random_user in dic_req:
            print (f"""
                   name: {dic_req[random_user]['info']['name']}
                   telephone: {dic_req[random_user]['info']['telephone']}
                   email: {dic_req[random_user]['info']['email']}
                    \n""")
            break
            
        