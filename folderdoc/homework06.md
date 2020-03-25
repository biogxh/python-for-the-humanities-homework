import json

#C:\\Users\\biogx\\GXH\\HW-05-data.json

def ReadJson(path):
    
    with open(path, 'r') as f:
        data = json.load(f)

    for element in data["items"]: # data is a list
        print("Title:___", element['title'])
        print("Authors:___", element['authors'])
        print("itemType:___",element['itemType'])
path = str(input('What is the path of json file?'))
ReadJson(path)
with open(path, 'r') as f:
        datadt = json.load(f)
i = int(input('Press 0 to add a new entry Press 1 to exit'))
while i != 1:    
    Titleinput = input("What is the title you want to type in for your entry?")
    Authorinput = input("What is the author you want to type in for your entry?")
    Typeinput = input("What is the item type you want to type in for your entry?")
    User_entry = {"title": Titleinput,
    "authors": Authorinput,
    "itemType": Typeinput,
    }
    temp = datadt['items'] 
    with open('C:\\Users\\biogx\\GXH\\HW-05-data.json', 'w') as json_file:
        temp.append(User_entry)
        datadt['items'] = temp
        json.dump(datadt, json_file)
    if i == 0:
        i = int(input('Press 0 to add a new entry Press 1 to exit'))