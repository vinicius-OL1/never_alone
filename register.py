import requests 
import json
def register ():
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/"
    user = dict()
    user["name"] = str(input('type your name: '))
    user["email"] = str(input("Type your e-mail: "))
    user["tel"] = str(input("enter your phone number: "))
    name = user["name"]
    email = user ["email"]
    tel = user["tel"]
    infor = {'info':{'name': name,'email': email, 'telephone': tel}}
    requests.post(f"{link}/user/.json",data= json.dumps(infor))
