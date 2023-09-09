import requests
import json
import random
#funtion for sortition one perfil for the user
def sortition():
    #variable for save the link of the database
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/user/.json"
    #variable for receive the information of the database
    req = requests.get(link)
    dic_req = req.json()
    #variable for save the user
    users = []
    #looping to scroll through the database content and save the user id
    for id_user in dic_req:
        #save the user id in the list
        users.append(id_user)
    #sortition one user
    random_user = random.choice(users)
    #looping for search the user in the database
    for id_user in dic_req:
        #condition for search the user in the database
        if random_user in dic_req:
            print (f"""
                   name: {dic_req[random_user]['info']['name']}
                   telephone: {dic_req[random_user]['info']['telephone']}
                   email: {dic_req[random_user]['info']['email']}
                    \n""")
            break
            
        