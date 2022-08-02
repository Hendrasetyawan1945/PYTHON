from pesertadidik import Mahasiswa 

class MahasiswaS1(Mahasiswa):
    def __init__(self, nama, alamat, nim,semester,skripsi):
        self.skripsi = skripsi
        super().__init__(nama, alamat,nim,semester)
       

    def __str__(self):
        return '{} || {} || {} || {} || {}'.format(self.nama, self.alamat, self.nim,self.semester,self.skripsi)


class MahasiswaS2(Mahasiswa):
    def __init__(self, nama, alamat, nim, semester, tesis,spp):
        self.tesis = tesis
        self.spp = spp
        super().__init__(nama, alamat, nim, semester)

    def __str__(self):
        return '{} || {} || {} || {} || {} || {}'.format(self.nama, self.alamat, self.nim, self.semester, self.tesis,self.spp)


class MahasiswaS3(Mahasiswa):
    def __init__(self, nama, alamat, nim, semester,penelitian):
        self.penelitian = penelitian
        self.gelar = "Doktor"
        super().__init__(nama, alamat, nim, semester)

    def __str__(self):
        return '{} || {} || {} || {} || {} || {}'.format(self.nama, self.alamat, self.nim, self.semester, self.penelitian,self.gelar)


alfida = MahasiswaS1('Alfida','Magelang','2021075','8','Sistem Gis')    
print(alfida)
annas = MahasiswaS2('Annas', 'Banten', '2018071', '4', 'Pemetaan tataruang kota','6000000')
print(annas)
biruu = MahasiswaS3('Biru', 'Tulungagung', '2018071', '5', 'Pemetaan tatan Global')
print(biruu)
