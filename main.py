import menu
from register import register
from login import login
import requests
import json

link = "https://never0alone-fa252-default-rtdb.firebaseio.com/"
while True:
    print (menu.options)
    choice = int(input("choose an option: "))
    if choice == 1:
        register()
    if choice == 2:
        my_user = str(input("enter your username: "))
        login(my_user)
    