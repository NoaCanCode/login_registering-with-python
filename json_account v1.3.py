#v1.3
'''
- Entering username is no longer cap sensitiive [V]
- Alnum func codes updated [V]
- Confm password when registering [V]
- Encrypting passwords in file [V]
'''

import json,time

#Encrytion func
def encrypt(inp):
    encrypted = ""
    for letter in inp:
        encrypted += chr(ord(letter)+75)
    return encrypted

#Decrypt func
def decrypt(inp):
    decrypted = ""
    for letter in inp:
        decrypted += chr(ord(letter)-75)
    return decrypted

# Confm alnum
def alnum(p,a,b,c): #(input,alpha,numeric,length)
    al = False
    num = False
    leng = False
    if a and b: #allows both alpha and numeric
        if p.isalnum() and len(p) >= int(c):
            return False
    elif a and not b: #allows only alpha
        if p.isalpha() and len(p) >= int(c):
            return False
    elif b and not a: #allows only numeric
        if p.isnumeric() and len(p) >= int(c):
            return False
    return True      

#Exists
def exists(inp):
    for k in content.keys():
        if inp == k.lower():
            return True
    return False #checks if input exists in file
            

#Login func
def login(user):
    file = open("accounts.json","r")
    contents = json.load(file)
    if exists(user):
        passwordl = decrypt(contents[user][0])
        upass = input("Enter password: ")
        for att in range(4):
            if upass == passwordl:
                return True
            else:
                print(f"incorrect! {3-att} attempts left!".title())
                upass = input("Enter password: ")
        return False
    else:
        print("error, username does not exist!".upper())
        return False

#Register func
def register():
    print(" #account creation# ".upper())
    file = open("accounts.json","r")
    content = json.load(file)
    username = input("Enter username: ") #Username
    while exists(username.lower()):
        print("username already exists".title())
        username = input("Enter username: ")
    print("##password creation##".upper())
    print(" #password must contain 10 characters, letters and numbers #".title())
    password = input("Enter password: ") #Password
    while alnum(password,True,True,10):
        print("Password entered does not fulfill requirements!")
        password = input("Enter password: ")
    confpass = input("Enter password again: ") #Enter password again
    while confpass != password:
        print("Passwords do not match!")
        password = input("Enter password: ")
        while alnum(password,True,True,10):
            print("Password entered does not fulfill requirements!")
            password = input("Enter password: ")
        confpass = input("Enter password again: ")
    content[username] = [encrypt(password)]
    file.close()
    file = open("accounts.json","w") #Save
    json.dump(content,file,indent=6)
    file.close
    print(f"Welcome {username}!") 
    time.sleep(1)


# Checking for past players
file = open("accounts.json","r")
content = json.load(file)
if exists("dummy"):
    file.close() #If file has no past accounts, clear file and create account
    print("welcome first user".upper())
    file = open("accounts.json","w")
    username = input("Enter username: ") #Username
    print("##password creation##".upper())
    print(" #password must contain 10 characters, letters and numbers #".title())
    password = input("Enter password: ") #password
    while alnum(password,True,True,10):
        print("Password entered does not fulfill requirements!")
        password = input("Enter password: ")
    while confpass != password:
        print("Passwords do not match!")
        password = input("Enter password: ")
        while alnum(password,True,True,10):
            print("Password entered does not fulfill requirements!")
            password = input("Enter password: ")
        confpass = input("Enter password again: ")
    content[username] = [encrypt(password)]
    info = {username.lower():[encrypt(password)]} #Saving user + password
    json.dump(info,file,indent=6)
    file.close()
    print(f"Welcome {username}!") 
    time.sleep(1)
else:
    a = input("Login/Register: ") #If file has past accounts, decide to login/create new
    while a != "login" and a != "register":
        a = input("Login/Register: ")
    if a.lower() == "login":  #Login
        if login(input("Enter username: ").lower()):
            print("Login successful! Welcome!")
        else:
            print("Login failed :<")
    else:
        register() #Registering
