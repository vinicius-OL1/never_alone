import requests
import json
#function to login
def login (user,password):
    #one variable to save the link of the database
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/user/.json"
    req = requests.get(link)
    #one variable for convert the json to dictionary
    dic_req = req.json()
    #loop for search user and password in the dictionary
    for id_user in dic_req:
        try:
            #condition for search user and password in the dictionary
            if user == dic_req[id_user]['info']['name'] and password == dic_req[id_user]['info']['password']:
                print (f"""
                       name: {dic_req[id_user]['info']['name']}
                       telephone: {dic_req[id_user]['info']['telephone']}
                       email: {dic_req[id_user]['info']['email']}
                          \n
                        """)
                break
        
        #condition for user not found
        except KeyError:
            print ("user not found")
            break
        
            