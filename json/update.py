import json

with open('crud.json', 'r') as file:
    data = json.load(file)

data['umur']=99
data['email']='manurun@gmail.com'

with open('crud.json', 'w') as tls:
    json.dump(data, tls, indent=4)