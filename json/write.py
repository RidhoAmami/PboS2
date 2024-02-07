import json

bio={
    "nama" : "manurun",
    "umur" : 100,
    "alamat" : "Jl. Texas lokal",
    "hobi" : ["mendengar musik", "menonton film"]
}

with open('crud.json', 'w') as tls:
    json.dump(bio, tls, indent=4)