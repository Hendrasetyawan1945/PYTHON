from staf import Staff

class Dosen(Staff):
    def __init__(self, nama, alamat,nip):
        self.nip = nip
        self.gaji = 5000000
        super().__init__(nama,alamat)
     
    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama, self.alamat, self.nip,self.gaji)


class Admin(Staff):
    def __init__(self, nama, alamat, nipA,gaji):
        self.nipA = nipA
        self.gajiA = gaji
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama, self.alamat, self.nipA, self.gajiA)
    

class CleaningServis(Staff):
    gaji = 3500000
    def __init__(self, nama, alamat, nipCS):
        self.nipCS = nipCS
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama, self.alamat, self.nipCS, self.gaji)
    
bambang = Dosen('Bambang','Tegal','987836')
print(bambang) 
anisa = Admin('Anisa', 'Aceh', '900006',4500000)
print(anisa)
sukarmi = CleaningServis('sukarmi','Sulawesi','679972')
print(sukarmi)
