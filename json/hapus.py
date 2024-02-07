import json

with open('crud.json', 'r') as file:
    data=json.load(file)

del data['umur']

with open('crud.json', 'w') as hps:
    json.dump(data, hps, indent=4)