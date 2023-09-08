import menu
from register import register
from login import login
from sortition import sortition
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
        my_password = str(input("enter your password: "))
        login(my_user,my_password)
    if choice == 3:
        print ("sortition...")
        sortition()