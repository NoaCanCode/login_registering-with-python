import json

#create file
new_file = open("accounts.json","w")
dummy = {"dummy":True}
json.dump(dummy,new_file,indent = 6)
new_file.close()
print("# files have been created! #".title())
