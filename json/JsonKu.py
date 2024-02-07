import json

class JsonKu():
    def baca(self, path):
        try:
            with open('crud.json', 'r') as file :
                data=json.load(file)
                print(data)
                return data
        except FileNotFoundError as lost:
            return "File Tidak Ditemukan: {}".format(lost)
        
    def tulis(self, path, perbarui):
        try:
            with open(path, 'w') as tls:
                json.dump(perbarui, tls, indent=4)
                print("Data telah ditulis ke dalam file.")
        except Exception as e:
                print("Terjadi kesalahan saat menulis file {}: {}".format(perbarui, e))

    def baru(self, path, key, value):
        data=self.baca(path)
        data[key]=value
        self.tulis(path, data)
        print(f"Data dengan kunci '{key}' telah diupdate.")

    def hapus(self, path,key):
        data = self.baca(path)
        if key in data:
            del data[key]
            self.tulis(path, data)
            print(f"Data dengan kunci '{key}' telah dihapus.")
        else:
            print(f"Tidak ada data dengan kunci '{key}' dalam file.")

pupun = JsonKu()

pupun.baca('crud.json')

bio={
    "nama" : "manurun",
    "umur" : 100,
    "alamat" : "Jl. Texas lokal",
    "hobi" : ["mendengar musik", "menonton film"]
}
pupun.tulis('crud.json', bio)
pupun.baru('crud.json', 'jenjang', 'smk')
pupun.hapus('crud.json', 'umur')
pupun.baca('crud.json')