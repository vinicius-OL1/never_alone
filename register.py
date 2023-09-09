import requests 
import json
def register ():
    #variable for save the link of the database
    link = "https://never0alone-fa252-default-rtdb.firebaseio.com/"
    #making a dictionary for save the user information
    user = dict()
    user["name"] = str(input('type your name: '))
    user["email"] = str(input("Type your e-mail: "))
    user["tel"] = str(input("enter your phone number: "))
    user["password"] = str(input("type your password: "))
    #transforming the dictionary to a simple variable
    password = user["password"]
    name = user["name"]
    email = user ["email"]
    tel = user["tel"]
    #passing information to the database
    infor = {'info':{'name': name,'email': email, 'telephone': tel, 'password': password}}
    #sending the information to the database
    requests.post(f"{link}/user/.json",data= json.dumps(infor))
