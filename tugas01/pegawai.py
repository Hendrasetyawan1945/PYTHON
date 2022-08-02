from staf import Staff

class Dosen(Staff):
    jabatan = "Rektor"
    def __init__(self, nama, alamat,nip):
        self.nip = nip
        super().__init__(nama,alamat)
     
    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama, self.jabatan,self.alamat, self.nip)


class Admin(Staff):
    jabatan = "Admin keuangan"
    def __init__(self, nama, alamat, nipA):
        self.nipA = nipA
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama, self.jabatan, self.alamat, self.nipA)
    

class CleaningServis(Staff):
    jabatan = "Staff Elit Kebersian Dunia"
    def __init__(self, nama, alamat, nipCS):
        self.nipCS = nipCS
        super().__init__(nama, alamat)

    def __str__(self):
        return '{} || {} || {} || {} '.format(self.nama,self.jabatan,self.alamat, self.nipCS)
    
bambang = Dosen('Bambang','Tegal','987836')
print(bambang) 
anisa = Admin('Anisa', 'Aceh', '900006')
print(anisa)
sukarmi = CleaningServis('sukarmi','Sulawesi','679972')
print(sukarmi)
